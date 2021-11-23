;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname ass7) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
;; Question 1

(define (subtract-min lst)
  (local
   [;; list-min: (listof Num) -> Num
    (define (list-min lon)
      (cond
        [(empty? (rest lon)) (first lon)]
        [else
         (local
           [(define res (list-min (rest lon)))]
           (cond
             [(<= (first lon) res) (first lon)]
             [else res]))]))
    
    (define min-val (list-min lst))

    (define (subtract-min-h lst)
       (cond
         [(empty? (rest lst)) (list (- (first lst) min-val))]
         [else (cons (- (first lst) min-val) (subtract-min-h (rest lst)))]))]
    
    (subtract-min-h lst)))

   
;;(subtract-min (list 6 3 2 4 1 9 7))
;;(check-expect (subtract-min (build-list 10000 add1)) (build-list 10000 identity))

;; Question2
(define (lenlen n)
  (local
    [;; digsum: Num -> Num
     (define (digsum n)
       (cond
         [(zero? n) 0]
         [else (+ (remainder n 10) (digsum (quotient n 10)))]))
     
     ;; len: Num -> Num
     (define (len n) (length (string->list (number->string n))))]

    (cond
      [(= n 0) 1]
      [(= n 1) 2]
      [else
       (local
         [(define ds (digsum n))
          (define res (lenlen (- n 1)))
          (define l1 (len res))
          (define l2 (len l1))]
         (+ ds res l1 l2))])))


;; Question3
;; A Point is a (list Num Num)

;; make-point: Num Num -> Point
(define (make-point x y) (list x y))
;; point-x: Point -> Num
(define (point-x pt) (first pt))
;; point-y: Point -> Num
(define (point-y pt) (second pt))


;; A Rectangle is (list Point Point)

;; make-rect: Point Point -> Rectangle
;; Requires:
;;  * (point-x bottom-left) < (point-x top-right)
;;  * (point-y bottom-left) < (point-y top-right)
(define (make-rect bottom-left top-right) (list bottom-left top-right))
;; bottom-left: Rectangle -> Point
(define (bottom-left r) (first r))
;; top-right: Rectangle -> Point
(define (top-right r) (second r))

(define (rectangle-sort lor)
  (local
    [;; calculate area of one rectangle
     (define (area r)
       (local
         [(define pbl (bottom-left r))
          (define ptr (top-right r))
          (define h (- (point-y ptr) (point-y pbl)))
          (define w (- (point-x ptr) (point-x pbl)))]
         (* h w)))

     ;; calculate distance p from origin (0, 0)
     (define (dis p)
       (sqrt (+ (sqr (point-x p)) (sqr (point-y p)))))
     
     ;; Predicate function 
     (define (r< r1 r2)
       (local
         [(define a1 (area r1))
          (define a2 (area r2))]
         
       (cond
         [(< a1 a2) true]
         [(> a1 a2) false]
         [else
          (local
            [(define r1bl (bottom-left r1))
             (define r2bl (bottom-left r2))
             (define r1tr (top-right r1))
             (define r2tr (top-right r2))]
            (cond
              
              [(< (dis r1bl) (dis r2bl)) true]
              [(> (dis r1bl) (dis r2bl)) false]
              [(< (dis r1tr) (dis r2tr)) true]
              [(> (dis r1tr) (dis r2tr)) false]
              [(< (point-y r1bl) (point-y r2bl)) true]
              [(> (point-y r1bl) (point-y r2bl)) false]
              [(< (point-y r1tr) (point-y r2tr)) true]
              [(> (point-y r1tr) (point-y r2tr)) false]
              [else false]))])))]

    (sort lor r<)))
    
(rectangle-sort
 (list
  (make-rect (make-point 0 0) (make-point 2 4))
  (make-rect (make-point 3 3) (make-point 4 4))
  (make-rect (make-point 0 0) (make-point 4 2))
  (make-rect (make-point 1 1) (make-point 2 2))))

          
