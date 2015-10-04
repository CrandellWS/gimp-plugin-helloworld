; [see ->](http://www.gimp.org/tutorials/Basic_Scheme/)
; for more in depth info on TinyScheme, a scripting interpreter
; [see ->](http://www.alphageeksinc.com/tinyscheme/documentation.html)
; Example command line calling GIMP in batch mode
; gimp-2.8 --verbose -d -i -b "(call_helloBatchWorldMessages 3)"


(define (call_helloBatchWorldMessages msgtype)
  (python-fu-helloBatchWorldMessagesPlugin RUN-NONINTERACTIVE msgtype)
)
