;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-intermediate-lambda-reader.ss" "lang")((modname a8) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
;; Question 1
(define (compatible-litres blood-bank blood-type)
  (local
    [(define (get-litres donor-blood)
       (cond
         [(symbol=? donor-blood 'O-) 0.5]
         [(symbol=? blood-type 'AB+) 0.5]
         [(symbol=? donor-blood blood-type) 0.5]
         [(and (symbol=? blood-type 'AB-)
               (or (symbol=? donor-blood 'A-)
                   (symbol=? donor-blood 'B-))) 0.5]
         [(and (symbol=? blood-type 'A+)
               (or (symbol=? donor-blood 'O+)
                   (symbol=? donor-blood 'A-))) 0.5]
         [(and (symbol=? blood-type 'B+)
               (or (symbol=? donor-blood 'O+)
                   (symbol=? donor-blood 'B-))) 0.5]
         [else 0]))]
    
    (foldr + 0 (map get-litres blood-bank))))


(compatible-litres (list 'O- 'O+ 'O- 'B- 'AB-) 'AB-)
(compatible-litres (list 'A+ 'B+) 'A-)
(compatible-litres (list 'A+ 'B+ 'AB+) 'AB+)


;; Question 2
(define (encode message)
  (local
    [(define chars (string->list message))
     (define letters (filter char-alphabetic? chars))
     
     (define uppers (map char-upcase letters))
     (define digits (map char->integer uppers))
     (define encrypt (map (lambda (n) (+ (- 90 n) 65)) digits)) ;; (90 - ord(c) + 65)
     (define new-chars (map integer->char encrypt))

     (define with-space
       (foldr (lambda (ch chrs) (cons #\space (cons ch chrs))) empty new-chars))

     (define str (list->string with-space))
     (define res (substring str 1))]

    res))

   
(encode "Cat")
(encode "A")
(encode "Is this correct?")

;; Question 3
(define-struct course (code number grades))
(define-struct summary (code number mean median failures))

(define (calculate-stats course)
  (local
    [(define (get-median lon)
       (local
         [(define len (length lon))
          (define mid (floor (/ len 2)))]
       (cond
         [(even? len) (/ (+ (list-ref lon mid) (list-ref lon (sub1 mid))) 2)]
         [else (list-ref lon mid)])))


     (define numbers (filter number? (course-grades course)))
     (define mean (/ (foldr + 0 numbers) (length numbers)))
     (define sorted (sort numbers <=))
     (define median (get-median sorted))
     
     (define failures
       (length (filter (lambda (g) (or (symbol? g) (< g 50))) (course-grades course))))]
    
    (make-summary (course-code course) (course-number course) mean median failures)))
     

(calculate-stats (make-course "CS" 115 (list 100 'DNW 30 0 75)))
(calculate-stats (make-course "ECON" 101 (list 60 70 50 90)))
(calculate-stats (make-course "MATH" 135 (list 76.5 0 91.5)))











