;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-abbr-reader.ss" "lang")((modname a7) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(define rolling-stone-2021
  (list "Respect"
        "Fight the Power"
        "A Change Is Gonna Come"
        "Like a Rolling Stone"
        "Smells Like Teen Spirit"
        "What's Going On"
        "Strawberry Fields Forever"
        "Get Ur Freak On"
        "Dreams"
        "Hey Ya!"))
;; 01
(define rolling-stone-2021-tweaked
  (list "Respect"
        "Hey Jude"
        "Fight the Power"
        "A Change Is Gonna Come"
        "Smells Like Teen Spirit"
        "Like a Rolling Stone"
        "What's Going On"
        "Strawberry Fields Forever"
        "Get Ur Freak On"
        "Dreams"))

(define (same-ranking song-lst1 song-lst2)
  (cond
    [(empty? song-lst1) empty]
    [(string=? (first song-lst1) (first song-lst2))
     (cons (first song-lst1)
           (same-ranking (rest song-lst1) (rest song-lst2)))]
    [else
     (same-ranking (rest song-lst1) (rest song-lst2))]))

(same-ranking rolling-stone-2021 rolling-stone-2021-tweaked)



;; 02
(define (sub-lst v n)
  (cond
    [(zero? n) empty]
    [else (cons v (sub-lst v (sub1 n)))]))

(define (expand-h lst i len)
  (cond
    [(= i len) empty]
    [else
     (cons (sub-lst (first lst) (add1 i))
           (expand-h (rest lst) (add1 i) len))]))

(define (expand lst)
  (expand-h lst 0 (length lst)))

(expand (list true 115 "a"))

;; 03             
(define (update full-vacc-lst new-vaccs)
  (cond
    [(empty? new-vaccs) full-vacc-lst]
    [(string<? (first (first full-vacc-lst)) (first (first new-vaccs)))
     (cons (first full-vacc-lst)
           (update (rest full-vacc-lst) new-vaccs))]
    [(string>? (first (first full-vacc-lst)) (first (first new-vaccs)))
     (cons (list (first (first new-vaccs)) (list (second (first new-vaccs))))
           (update full-vacc-lst (rest new-vaccs)))]

    [else
     (cons (list (first (first full-vacc-lst))
                 (append (second (first full-vacc-lst)) (list (second (first new-vaccs)))))
           (update (rest full-vacc-lst) (rest new-vaccs)))]))
       
    
(update (list (list "Graham" (list "May 15, 2021" "June 25, 2021" ))
              (list "Kaplan" (list "June 1, 2021" "July 1, 2021"))
              (list "Vasiga" (list "July 10, 2021"))
              (list "Zoo" (list "July 10, 2021")))
        (list (list "Pretti" "July 17, 2021")
              (list "Vasiga" "July 22, 2021")))


