;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname module5) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; 05.1.2
(define mirepoix (cons "onion" (cons "carror" (cons "celery" empty))))
mirepoix

;; 05.1.6
(define (starts-with-3? lon)
  (cond
    [(and (cons? lon) (= (first lon) 3) true]
    [else false]))

;; 05.1.7
(define (swap lst)
  (cons (first (rest lst)) (cons (first lst) empty)))

;; 05.2.1
(define (extnum? val)
  (cond
    [(number? val) true]
    [(equal? val 'infinity) true]
    [else false]))

;; An ExtNum is one of:
;; * A Num
;; * 'finitiny

;; extnum-template: ExtNum -> Any
(define (extnum-template n)
  (cond
    [(number? n) ...]
    [else ...]))

;; A (listof Num) is one of:
;; * empty
;; * (cons Num (listof Num))


;; 05.3.3
(define (average lon)
  (/ (sum-list lon) (length lon)))


;; 05.3.4
(define (has-goose? los)
  (cond
    [(empty? los) false]
    [(symbol=? (first los) 'goose) true]
    [else (has-goose? (rest los))]))

;; ('vc 'alice 'goose 'bob 'nick)



;; 05.4.1
(define (mult-list lst)
  (cond
    [(empty? lst) 1]
    [else (* (first lst) (mult-lst (rest lst)))]))


;; 05.4.2
(define (glue-strings los)
  (cond
    [(empty? los) ""]
    [else (string-append (first los) (glue-strings (rest los)))]))

(glue-strings (cons "vc" (cons " " (cons "good"))))




;; 05.4.4
(define (shout-list los)
  (cond
    [(empty? los) empty]
    [else (cons (string-upcase (first los))
                (shout-list (rest los)))]))



;; 05.4.5
(define (eats-apple los)
  (cond
    [(empty? los) empty]
    [(symbol=? (first los) 'apple) (eats-apple (rest los))]
    [else (cons (first los) (eats-apple (rest-los)))]))



;; 05.4.6
(define (renormalize lon)
  (cond
    [(empty? lon) empty]
    [(number? (first lon)) (cons (first lon) (renormalize (rest lon)))]
    [else (renormalize (rest lon))]))



;; 05.5.1
(define (snoc n lon)
  (cond
    [(empty? lon) (cons n empty)]
    [else (cons (first lon) (snoc (rest lon)))]))


    
;; 05.5.2
(define (count lst val)
  (cond
    [(empty? lst) 0]
    [(equal? (first lst) val) (+ 1 (count (rest lst) val))]
    [else (count (rest lst) val)]))

;; (count (1 3 2 3) 3) -> 2
;;   = (count (3 2 3) 3) -> 2
;;        = (+ 1 (count (2 3) 3)) -> 2
;;                  = (count (3) 3) -> 1
;;                       = (+ 1 (count () 3)) -> 1
;;                                 -> 0



;; 05.5.3
(define (all-even? lon)
  (cond
    [(empty? lon) true]
    [(= (remainder (first lon) 2) 1) false]
    [else (all-even? (rest lon))]))


    
    





    