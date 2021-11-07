;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname a6) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(define (trial-division k n)
  (cond
    [(> (sqr k) n) true]
    [(zero? (remainder n k)) false]
    [else (trial-division (add1 k) n)]))

(define (prime? n) (trial-division 2 n))

(define (goldbach-pairs n)
  (helper 2 n empty))

(define (helper i n pairs)
  (cond
    [(> i (/ n 2)) pairs]
    [(and (prime? i) (prime? (- n i)))
     (cons (list i (- n i)) (helper (add1 i) n pairs))]
    [else (helper (add1 i) n pairs)]))

(goldbach-pairs 4)
(goldbach-pairs 10)
(goldbach-pairs 60)


;; 02
(define (string-split i s)
  (cond
    [(string=? (substring s i (+ i 1)) " ") (list (substring s 0 i) (substring s (+ i 1)))]
    [else (string-split (add1 i) s)]))

(define (insert course courses)
  (cond
    [(empty? courses) (list course)]
    ;; [(string<=? course (first courses)) (cons course courses)] 
    [(string<? (first (string-split 0 course)) (first (string-split 0 (first courses))))
      (cons course courses)]
    [(and (string=? (first (string-split 0 course)) (first (string-split 0 (first courses))))
          (<= (string->number (second (string-split 0 course))) (string->number (second (string-split 0 (first courses))))))
     (cons course courses)]
    [else (cons (first courses) (insert course (rest courses)))]))


(define (sort-courses courses)
  (cond
    [(empty? courses) empty]
    [else (insert (first courses) (sort-courses (rest courses)))]))

(sort-courses (list "GOOSE 123" "DS 11" "CS 116" "CS 99" "DS 11" "CS 115"))



(define (my-sort lon)
  (cond
    [(empty? lon) empty]
    [else (insert (first lon) (my-sort (rest lon)))]))



;; 03

;; Constructor
(define (make-pair key val) (list key val))
;; Selectors
(define (pair-key p) (first p))
(define (pair-val p) (second p))

(define (al-add key dict)
  (cond
    [(empty? dict) (list (make-pair key 1))]

    [(equal? key (pair-key (first dict)))
     (cons (make-pair (pair-key (first dict)) (add1 (pair-val (first dict)))) (rest dict))]
    
    [else (cons (first dict)
                (al-add key (rest dict)))]))

(define (build-histogram los)
  (cond
    [(empty? los) empty]
    [else (al-add (first los) (build-histogram (rest los)))]))

(build-histogram (list 'dog 'cat))

(build-histogram (list 'apple 'pear' peach 'apple 'apple 'pear))













