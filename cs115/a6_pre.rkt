;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname a6_pre) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; Question 1
(define (faro-shuffle lst0 lst1)
  (cond
    [(empty? lst0) lst1]
    [(empty? lst1) lst0]
    [else (cons (first lst0) (cons (first lst1) (faro-shuffle (rest lst0) (rest lst1))))]))


(faro-shuffle (list "a" "b" "c") (list "A" "B" "C"))
(faro-shuffle (list 1 3 5) (list 2 4 6 8 10))


;; Question 2
(define (factorial n)
  (cond
    [(zero? n) 1]
    [else (* n (factorial (- n 1)))]))

(define (com n k)
  (/ (factorial n)
     (* (factorial k) (factorial (- n k)))))

(define (line n k)
  (cond
    [(= k n) (list (com n k))]
    [else (cons (com n k) (line n (+ k 1)))]))


(define (pascal_h i n)
  (cond
    [(= i n) empty]
    [else (cons (line i 0) (pascal_h (+ i 1) n))]))

(define (pascal n)
  (pascal_h 0 n))

(pascal 5)



;; 7.4
(define (merge-unique lst1 lst2)
  (cond
    [(empty? lst1) lst2]
    [(empty? lst2) lst1]
    [(= (first lst1) (first lst2))
     (merge-unique (rest lst1) lst2)]
    [(< (first lst1) (first lst2))
     (cons (first lst1) (merge-unique (rest lst1) lst2))]
    [else
     (cons (first lst2) (merge-unique lst1 (rest lst2)))]))


;; Question 3
(define (merge-lists list1 list2)
  (cond
    [(empty? list1) list2]
    [(empty? list2) list1]
    [(string=? (first list1) (first list2))
     (merge-lists (rest list1) list2)]
    [(string<? (first list1) (first list2))
     (cons (first list1) (merge-lists (rest list1) list2))]
    [else
     (cons (first list2) (merge-lists list1 (rest list2)))]))

   
(define (merge-dicts dict1 dict2)
  (cond
    [(empty? dict1) dict2]
    [(empty? dict2) dict1]
    [(string=? (first (first dict1)) (first (first dict2)))
     (cons (list (first (first dict1)) (merge-lists (second (first dict1)) (second (first dict2))))
           (merge-dicts (rest dict1) (rest dict2)))]
    [(string<? (first (first dict1)) (first (first dict2)))
     (cons (first dict1) (merge-dicts (rest dict1) dict2))]
    [else
     (cons (first dict2) (merge-dicts dict1 (rest dict2)))]))

(merge-dicts
 (list
  (list "ball" (list "FR balle"))
  (list "house" (list "FR maison" "UK ..."))
  (list "resist" (list "CA resistir" "UK ...")))
 (list
  (list "apple" (list "CA poma" "FR pomme" "UK ..."))
  (list "ball" (list "FR ballon" "UK ..."))
  (list "house" (list "DE Haus" "FR maison"))))



  
    




    
                    
                    



   