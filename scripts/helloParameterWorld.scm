; [see ->](http://www.gimp.org/tutorials/Basic_Scheme/)
; for more in depth info on TinyScheme, a scripting interpreter
; [see ->](http://www.alphageeksinc.com/tinyscheme/documentation.html)
; Example command line calling GIMP in batch mode
; gimp-2.8 --verbose -d -i -b "(call_helloBatchWorldMessages 3)"


(define (call_helloParameterWorld v0 v1 v2 v3 v4 v5 v6 v7 v8 v9 v10 v11 v12 v13 v14 v15 v16)
  (python-fu-helloParameterWorldPlugin RUN-NONINTERACTIVE v0 v1 v2 v3 v4 v5 v6 v7 v8 v9 v10 v11 v12 v13 v14 v15 v16)
)
