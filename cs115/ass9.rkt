;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname ass9) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; ============ Question 1 =============
(define-struct stock (name price high low volume))
;; A Stock is a (make-stock Sym Num Num Num Nat)
;; Requires: 0 <= low <= price <= high

(define-struct timestamp (hours minutes seconds))
;; A Timestamp is a (make-timestamp Nat Nat Nat)
;; Requires:
;;  * hours < 24
;;  * minutes < 60
;;  * seconds < 60

(define-struct order (stockname price quantity time))
;; An Order is a (make-order Sym Num Nat Timestamp)
;; Requires: price >= 0

(define (process los ord endtime)
  (local
    [(define (update s)
       (cond
         [(symbol=? (stock-name s) (order-stockname ord))
          (make-stock (stock-name s)
                      (order-price ord)
                      (max (stock-high s) (order-price ord))
                      (min (stock-low s) (order-price ord))
                      (+ (stock-volume s) (order-quantity ord)))]
         [else s]))
     
     (define (later? t1 t2)
       (cond
         [(< (timestamp-hours t1) (timestamp-hours t2)) false]
         [(> (timestamp-hours t1) (timestamp-hours t2)) true]
         [(< (timestamp-minutes t1) (timestamp-minutes t2)) false]
         [(> (timestamp-minutes t1) (timestamp-minutes t2)) true]
         [(< (timestamp-seconds t1) (timestamp-seconds t2)) false]
         [(> (timestamp-seconds t1) (timestamp-seconds t2)) true]
         [else true]))]
    
    (cond
      [(later? (order-time ord) endtime) los]
      [else (map update los)])))

(define bmo (make-stock 'BMO 137.89 139.35 137.75 140000))
(define telus (make-stock 'T 29.13 29.13 28.915 888000))
(define pow (make-stock 'POW 42.94 42.99 42.40 45000))
(define cantire (make-stock 'CTC 298.00 305 298 500000))

(define stocks (list bmo telus pow cantire))

(define 330pm (make-timestamp 15 30 00))
(define almost5pm (make-timestamp 16 59 59))

(define t-order (make-order 'T 29.10 2000 330pm))
(process stocks t-order almost5pm)

;; ============ Question 2 =============
(define-struct card (rank suit))
(define as (make-card 'ace 'spades))
(define ks (make-card 'king 'spades))
(define kh (make-card 'king 'hearts))
(define qs (make-card 'queen 'spades))
(define qd (make-card 'queen 'diamonds))
(define js (make-card 'jack 'spades))
(define jc (make-card 'jack 'clubs))
(define 10c (make-card 10 'clubs))
(define 7s (make-card 7 'spades))
(define 6c (make-card 6 'clubs))
(define 2d (make-card 2 'diamonds))
(define 2c (make-card 2 'clubs))

(define hand1 (list as ks qs js 7s kh 2d 6c 2c))
(define hand2 (list as kh qd jc))
(define hand3 (list 10c 6c 2c))
;; -------------------------

(define (point-count bridge-hand)
  (local
    [(define (same? suit) (lambda (c) (symbol=? (card-suit c) suit)))
     (define s-count (length (filter (same? 'spades) bridge-hand)))
     (define h-count (length (filter (same? 'hearts) bridge-hand)))
     (define d-count (length (filter (same? 'diamonds) bridge-hand)))
     (define c-count (length (filter (same? 'clubs) bridge-hand)))

     (define (count->point count)
       (cond
         [(= count 0) 3]   ;; void
         [(= count 1) 2]   ;; singleton
         [(= count 2) 1]   ;; doubleton
         [else 0]))
         
     (define (rank->point c)
       (cond
         [(equal? (card-rank c) 'ace) 4]
         [(equal? (card-rank c) 'king) 3]
         [(equal? (card-rank c) 'queen) 2]
         [(equal? (card-rank c) 'jack) 1]
         [else 0]))

     (define rank-points (foldr + 0 (map rank->point bridge-hand)))]

  (+ rank-points
     (count->point s-count)
     (count->point h-count)
     (count->point d-count)
     (count->point c-count))))

(point-count hand1)
(point-count hand2)
(point-count hand3)


;; ============ Question 3 =============
(define x (+ 5 1))
(define y (* (+ 3 2) (- x 4)))
(define z (* (+ 3 y) x))

(define-struct opnode (op arg1 arg2))
;; An OpNode is a (make-opnode (anyof '+ '- '* '/) BinExpExt BinExpExt)

;; A BinExpExt is one of:
;; * a Num
;; * a Sym
;; * an OpNode
(define-struct definition (id exp))
;; A Definition is a (make-definition Sym BinExpExt)

(define sample-defns
  (list (make-definition 'x (make-opnode '+ 5 1))
        (make-definition 'y (make-opnode '*
                                         (make-opnode '+ 3 2)
                                         (make-opnode '- 'x 4)))

        (make-definition 'z (make-opnode '*
                                         (make-opnode '+ 3 'y)
                                         'x))))
;; -----------------------------
(define (constant-value definitions id)
  (local
    [(define (eval exp)
       (cond
         [(number? exp) exp]
         [else
          (local
            [(define op (opnode-op exp))
             (define v1 (eval (opnode-arg1 exp)))
             (define v2 (eval (opnode-arg2 exp)))]
            (cond
              [(symbol=? op '+) (+ v1 v2)]
              [(symbol=? op '-) (- v1 v2)]
              [(symbol=? op '*) (* v1 v2)]
              [else (/ v1 v2)]))]))
     ;; ------------------------
     (define (id->exp id)
       (definition-exp (first (filter (lambda (d) (equal? (definition-id d) id)) definitions))))

     (define (build exp)
       (local
         [(define (get-child exp)
            (cond
              [(number? exp) exp]
              [(symbol? exp) (build (id->exp exp))]
              [else (build exp)]))
          (define op (opnode-op exp))
          (define arg-l (get-child (opnode-arg1 exp)))
          (define arg-r (get-child (opnode-arg2 exp)))]
         (make-opnode op arg-l arg-r)))]
          
    
    (eval (build (id->exp id)))))

(constant-value sample-defns 'x)
(constant-value sample-defns 'y)
(constant-value sample-defns 'z)







