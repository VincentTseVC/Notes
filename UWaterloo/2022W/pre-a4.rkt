;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname pre-a4) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; Question 1

(define (count val lst)
  (cond
    [(empty? lst) 0]
    [(equal? val (first lst)) (add1 (count val (rest lst)))]
    [else (count val (rest lst))]))

(define (list->set lst)
  (cond
    [(empty? lst) empty]
    [(= (count (first lst) lst) 1) (cons (first lst) (list->set (rest lst)))]
    [else (list->set (rest lst))]))

(list->set (cons 17 (cons "A" (cons 42 (cons "A" (cons false empty))))))

;; Question2
(define (char->nat ch)
  (cond
    [(and (char>=? ch #\0) (char<=? ch #\9))
     (- (char->integer ch) (char->integer #\0))]))

(define (helper loc res)
  (cond
    [(empty? loc) res]
    [(char=? (first loc) #\+)
     (helper (rest (rest loc)) (+ res (char->nat (first (rest loc)))))]
    [else
     (helper (rest (rest loc)) (- res (- (char->integer (first (rest loc))) 48)))]))


(define (add-sub-string s)
  (helper (string->list s) 0))

(add-sub-string "+3")
(add-sub-string "+3+4-5")
(add-sub-string "-5+3+4-6-6")


;; Question3
(define (q3-helper loc points)
  (cond
    [(empty? loc) points]
    [(and (>= (length loc) 2)
          (char=? (first loc) #\I)
          (char=? (first (rest loc)) #\J))

     (q3-helper (rest (rest loc)) (+ points 4))]

    
    [(or (char=? (first loc) #\A)
         (char=? (first loc) #\E)
         (char=? (first loc) #\I)
         (char=? (first loc) #\N)
         (char=? (first loc) #\O)) (q3-helper (rest loc) (+ points 1))]
    
    [(or (char=? (first loc) #\D)
         (char=? (first loc) #\R)
         (char=? (first loc) #\S)
         (char=? (first loc) #\T)) (q3-helper (rest loc) (+ points 2))]
    
    [(or (char=? (first loc) #\B)
         (char=? (first loc) #\G)
         (char=? (first loc) #\K)
         (char=? (first loc) #\L)
         (char=? (first loc) #\M)
         (char=? (first loc) #\P)) (q3-helper (rest loc) (+ points 3))]
    
    [(or (char=? (first loc) #\F)
         (char=? (first loc) #\H)
         (char=? (first loc) #\J)
         (char=? (first loc) #\U)
         (char=? (first loc) #\V)
         (char=? (first loc) #\Z)) (q3-helper (rest loc) (+ points 4))]
    
    [(or (char=? (first loc) #\C)
         (char=? (first loc) #\W)) (q3-helper (rest loc) (+ points 5))]
    
    [(or (char=? (first loc) #\X)
         (char=? (first loc) #\Y)) (q3-helper (rest loc) (+ points 8))]

    ;; Q
    [else (+ points 10)]))
    
  
(define (scrabble-scoren word)
  (q3-helper (string->list word) 0))



(scrabble-scoren "ONE") ;; 1 1 1 -> 3
(scrabble-scoren "DIJKSTRA") ;; 2 4 3 2 2 2 1 -> 16

















  