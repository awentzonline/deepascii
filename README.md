deepascii
=========
Generates ASCII art from images using features extracted from a deep neural net (VGG16)

Install
-------
`pip install deepascii`

Usage
-----
Basic usage: `make_deepascii.py --font=<FONT_FILENAME> <IMAGE_TO_TRANSFORM>`

A monospaced font (DroidSansMono.ttf) is included in the examples directory.

There are a number of options:

 * `--font-size` Tweak font size to fit your terminal
 * `--layer` Name of VGG16 layer to take features from
 * `--pool` Integer downscaling factor
 * `--pool-type` Type of pooling (avg or max)
 * `--invert-color` Invert to assume black text on a white background

Examples
--------

![Steve Buscemi](https://github.com/awentzonline/deepascii/raw/master/examples/images/steveb.png)

```
                 _/1__wdPP1N 1 NN T  M 1T17 wKW_VNT __mNTTT _$WN$F$____            
             _/ y1_4_____wwmw    T  1 d  $Wf _y$M _ __4F __mF_  ___MNNNme_         
              _|$4P___Z$NNm 1     d|  4    $_MNF dFW$ _/Wf _fF_4NP _mmm_ Nk_       
              4$F_WP______     \   \        4    $ TF $WT M$M 4$   4_  N_ N$L      
            _|$_4__w4MPTNN            m           $  1   4    T1W1 11__ __ $$L     
           _ $L_J _J _mRNF             +                              $__$_ $NL    
           1 $mF JT __ _k `                                4   /       1NN1__$NL   
          |_ _pF___wP_/`_K                                               mmL_NN$L  
           |_f dK_$MWRkWP                                                $m_ |_V$L 
           $  4__N _F_y                                                   $1  $_4L 
         | $___4P dFWNN                                                   $L h_$N4L
         | _ 14__P__uK _                                                  T   T$__\
        _| |14 1__A1 _N      y                                            4  __ |Nk
        4$ 4N11 TNK_m_ _                                                     4$_4jF
         $L`$PH$_PWP F 5/                                                  4_ _$_$ 
         $L  . TF wP __LN                                                   1_ q4K 
           _m 4KJ __NKF                                                    | T $$  
      __  A$pwmN aME                                                       4_ aF/  
      1RL  ` $NWmP_1       4   _        x   ___                            j$_`    
        7\    f __f           M w WP  __fMmmNNmk              _____ __ _   4$/     
          \   a4NF         M1   __w##P``~#     __            WMMMMNkK_ $L_ 4$\x    
           $    __       $     dP __awwmw__x.  _$k       _ ww__..___  1 `$ j$y     
      |    qL   4$K             #K 4 mwNk 1k_ MN$       yRNmP ______\u_ 3  $N      
      |     $P  4k              $   Am#F    _$  y      4F wm  7C.Z$ \_1W   $       
      1         `                  + x ww    J 4       4  mm  \C_JF  TL   j$       
       |      |     y                     w#                        wP$   4 \      
        \  \v_                                         |      w __ m      T $      
       |     1       +                                                    $j       
        $     $                                                          j$/       
         \_                                 y                           d4/        
          `+wwm        +                   |                           1 _         
              $         4                  \______      _               _4         
              1     4                 P     `TTTPMk_ __amw             a/          
              |$y                                  NMNR               j            
              |        |             /     _               x          $            
              |  __    $         /      _   ____          m       4  4             
                  $_   4           _uamK`_____     wmwmw _   _4     jF             
           __ak   T$_   |   $   4      `$L```P##mwmwwmmw _aw@_$    y/              
         _d1N4L     4L _     v   f        TNkm w    __ wm`   7   _/$               
         4$__4k      $mk                 m________       J  _  _m`y                
       _  $1_4L       4$___                TNNMNMMwmwmwP    $w#` 4                 
      y1  1 _4k        I $_ ww                           #    # 7                  
     y$L  1_4$          $_Nk_  Mk v             `    +  1  4_ _/                   
    y1L__  $N$     m     $__$_e wmk_                     ___ _`                    
  _4$__      _            T$N1j__\ _x            __       4M jL                    
  4$_1N __ $ 4k              N$WNw-___L         wP      _|1  4$L                   
 4$NL __4N JL4L                1N$_$Nwkk____/_ __ ____uNPP  _$NNL                  
 1mN$ 4NL  _$W1                   TNmw__NP4Wwm4_$wWM#F $    4$NNNk___              
M _ _______ N$_k           `       _   1Nmmh#+MP`1   m_     $N_NL_ Nkp_______ 
```

```

                                                    _ yd/AP  ______.JwwWWMMNNNNNKKCZZ   $$    7$$W 7T TTP7PF  $VVP` WJ1M71NNTRWVM7T`__.W/C5$WM+__ywM#PPT```    ___.w/A Z$$7TNTPTTTT`  TTZZII$Nwm~~jFFF__lL____  y                                          
                                            _yv/ ___y//PP______awwwmddZZ2P_  `TT19++wwZJ1NNLW N$1kK    1   __JM41F  WJTT 1 __lJfF___am/FFWV/___yV/A$$T   .  ___aam+fC$_4P+__JTP   _____pwmww+PKTCZ$ILN444kL_____4LL______                                  
                                          __y/   __d41C` aawwwdMMMMPPF++________ ____h+rCN41P  7TF         _y/PT1  _j|P     qmr __uW/PF  J __yy/fC$7/    ~__.aW+fT$__aJKK uV/  _____apmPRPPN$$Nwnmm+hWfff5hmmmwuamku________                               
                                        __yy/   _j44PA___d$$$NP`_______Il__pww..pamm.27$kWZT    T  j;      4fF `1  W41F    _j$1 uadfFC   ___y/AC$y/KC_____ v/f``___uJ#FF  Y/_____awm#PF___    j$PP________d$MNNNMNNhmmmee____                              
                                       _yyx/  __44/PC___pw++_______uaagggjigP~+mVdf$hk  1L         7TL  __J7T      df1     47/hWJPFC_   ___J/K$aV/F yvmLyW/KC____aa#PF__  ____aad##PF___..  _$ ________pwMMPPPNTNNNNNNNNhkeL____                           
                                      _yV/F  __y4/$$_aamKKC$$uwwwmm#fhKNN4AKCZZ_  4T1NLNJRkF       $|  _uxZ`    _  471     ~fF VTC$m+ _ wa4fC$V/PF  JZ$VX ___apww#/F___y/___amm#PF ___.xmKL  ______aap#PP __________TTT77NMkkL____                         
                                      y//`  __y41A$4dMNPP ++++______IIIlNN$hhmu..  $$N NPP         4|  \VJ$     wvW4$L    TT`  $$WVPF__WWfT$NV/F`  /Ayx/F uudfPPP``__av/__WdMPPF  __am#6$F ___jywwNM#PF_____appw_______  77NMhmmp_                         
                                     y//  ___||/ U4mmPP________..wwwwwmmmHmHNNhhkL 71F       y/    `\ dJ\Q|     `1 3$|    4r   7qJ$KwWamMA VfTF  WXAU7fF WWd$$FF  _ag/F WW44PF  __aV/F$D/  __a4fNUMfF  yrqjmHNNNNNNNLL_____77NN$kL__                       
                                     4   __yd41L_JfPPF___uaawwmmM##RR#RRNNTTFT7P1L           T      \\V/A\xL       d$$L   7$ W/ N71NWN2ZF   `  _W/ANV$F  JJ441F   W4fF Wd4fFF  _wdJZCLV/  __j44$NYP   JfANJZ11111NNN1N___nwVNT7$$kLL_                      
                                    4/  __/|41$$VPP___ wMM##PP_________       ZZ$        \k d$L __  `3+  `\\L__    4$$k   `     J1  d44F       V/  d4F  WVP#$1F  W44$L W4$TF  WdAHf$ux/   ud4$$NPF    4| 4|$____   J1NNL_N1  JTNN$$LL_                     
                                   4    y44l$$VPA____W4PP```` ....___________g~++~  ~~+  PF  4+K  _  ``   `1\VcC___ 77          7   V71L      JfF  dTF WJTP `` __ d$$kWdfPF  WJTRT$NMfKWWwmd4$RKF __  11W4$$L__      NNNm____JTNNM$$kL_                    
                                _y    _y/4|fP+KC__apprF _____ggg~tppaaawwmwwmKTTT  4TD1k `   `` Wmmk        3f+   ____              T7`\     7TT   71 _        avW7TP W4TT    4    TT1hVWNTN$$PF  W4;    J11mm____     N41Nww  NNN7P\\L_                   
                                y/   _y/ |I$ZI__Wd$PP_____..JZ$$wwmm#PPjN$NNRk     ~~      \L   JP#+  ww     $ ` amxmx ___          TT ~\    71       $V/      4$VNT   71   _Jf       d1PN197fF  Wd4L    41PHN$___    __Z____   NJ$CN$kk                   
                               y/   _j/|_JlmmmcpJP____wawm+++tMMNNPTTCC$ZkL_       ``      ~~~++   _           WW4ZZ ~+www          `  ``     1       ~~       J$1          441       41   T7`1  WM$$L  d41  14$L___    4$u_____ 4TNU4$L___                
                              W/   _y/| j|PFN$$PZC5wwdM#KKC$$PPF  ___ggdfNkkkP               ```                A++K C2__                        |    TT     + 27T     `    `T        T1        fPPT1   77    11$mL___  NNNhLLL_   $$Z$kkxL_               
                               ` __y/4 W4$L__7___ydKNPP___gppfFF___aamAFFNNKFF  ___                + ww          `` ~+mwu   ______  ___   +      |  . ~\     T$$Z            T     4  `1        T   T   4T     T1$$mL___  NNj|k    d4$$DN4kL_              
                                 _|/1  dJ$hk___aJZP ____.J4PP __$ammPP_$$NPP  __ wx/               `                 ``~~+ wwwwww         `  __ 31    `2      $$$                  `   \       71      d41N      71$$L_____N4IL___  T4$|N$$\L_             
                                _j|1  jj$P__$uw#AKL  aam++~;  wa+PF`C../__``  wv/#RL                                         `#P#~  ++~        w41    +s$      $$4       +            W41      71  `    7          11$$L____4$mmpL   74$UJ4$kLL            
                                y41   471__uw#KFC __WdfTC55   /``_   ~__$.   W#+F                                                                     `             ___  `        aZ   `+    3J/                    T1$$NNNNNNPPFk___ jj|_N4$\L_           
                               j4f1h  4$$uV#PFCL  _WJZT_    _____.//C$$xrnk ~KC`                                                                                  \    .          4$   ``   +4+F                      11NJN1 ZZIILNwL__j$L.N$$\L__         
                               ||T$ Y _jVMPF__zr  WmfF   ____..wr/C_ymffFL_ CL                                                                      `   wmm         Mmmwv         `1        `T`                w       111_________A\k.JA\Luj$$kkL         
                              ||| _J  jJT___am/F  jI$_____.wwm+KK__W/PF`__ mn                                                                                         ``                                       1\\       $_mmm44ZLL__~+V7A$V7AN$kkL        
                             _j| _j|  JZ__aV/F_____ ___uwwm#FFC__am/F  _ggpKK                                                                                                                                            144|NNNhhmm-``  7A\|N4$$LLL       
                             J41 q||  4_ud#PF__axpr _uV##K$$L _ym/F__  a4$LL                                                                                                                            v                 1$$____NN1kkL__  j$L`$$m\L       
                             4f1 d|L _j$MfFF _dd4KL__4ZCL_mmkWWfKKLLkWW#9Rkk                                                                                                                                               4$mL_____  +qL__J4Lu77N$\L      
                            J||  J|k ud4PF _WdMPRLLWdJAkm#PPLW4$kkw+KLL777`                                                                                                                                                T1$$kmmpp   5$___A\VK__J$k      
                            44$  4$| WdfF __J4$TNwmmjrPTTP`__J7PP ___                          $                                                                                                                            1$|PNNNLL  4444LL`1_ajZ|k      
                            |11 N4$| _Z` _WdfP1___Z$$1k   _yrP ____..  __          ___        /                                                                                                                             14$L_Z1K___ ff$|L__ N4$L_      
                             |  W4$|Ww:  q4PK ____wmrF ___JfFL___gmrK  vx/                                                                                                                                                   4$$$ET  k__  4$lL___A$$L_     
                           jjy   $$|WA1L J1C____dNNTF  _yg/FF wwmMP1L_ /CL          N4                                                                                                                                       T$$$kL  \\L__J$$mLL__J\\L     
                          _|7T    41L j| J1 _J4N4MPK___Wj$$L___N1kK_y/K                 y              +                                                                                                                      T$$E|_  4$k__7PfNhhVZA4LL    
                          _|   ___7$| _|L __J4_jPF _yrWd$RkLwwWPZ_$V/FL          -      4       `     ``                                                                                                                      4$$NmLL `11KL___ITNNVN4$LL   
                          j|   4a  j|Ww$;__J4$4$F __JCN4fF_|P____W/PF   y    v   `                                                                                                                                            j4$PP\k    f4muw4Z_J1WN4\LL  
                          j|;  ff|_j|NN41WJ4$PP+___Jrk P_______pp/FC  __|L                                                                                                                                                    7T$L `1     71NN$$____23$\L  
                         _j$;  ____41L `|V4ZP_____JfF __uammuamrFF__  wavk                                                                                                                                                     4$FK ___     $$1q$ium_2$$k  
                         W4fF   qirA$LL__Z$$k_uwwm#F __JWd$$WMfFF  ypWW#KK              _                                                                                             .                                        J$|  \x___   Z 1$$1NNNj4$L  
                         _j$|   4$LNA+kWj|P _jVPPP___yx/A$$PPP`___41kKF``___            xx    __                                                                                     m+                                        4$$L  1\___     4$CUNN4$$k  
                         _j$;   4$|__`1U41L_jJTK___.W/`594PF   _.wN1k    wm+k           f+                                                                                            `                                        Jffk   4|ax___  4$$_ N4fPk  
                         j4fL    1$y;w4VP1LWJPF_yym+KC__/`_____dAKN1F  W##f`  .         `                                                                                                                                       ``    J4fA\V_  A4|L__4$F   
                         44$LL   j$$|N4fCLWV/C_J4TCC5ax/ __yamKPCIL    _C_    +       4                                           _                                                                                                     $2|\L__ 4$LL_j$K   
                         |$$$LL  44$|WJ1kW4f__Wdf1kWW4PF WVd#PF__y- __.$     ``       j$                                                               _                                                                          _     4$MN$iL J4$LNj/F   
                         |7j$Lk   4$1L ZLJ$$WW4$P _UJTF _j4FF___J/L_pmwc|L            x                                                                                          .                                               ____   J11N4AkL_`$$N4K    
                           4$$LL  Af$LJwh+wNmmm1  W441LWWJZF \v/KL x/`C$y//           `                                                                                         ++                                               \qq._    _ZZI$L__4$jJF    
                         | d$$kk  `T$MFP    _$____JPPF W++____XC$W `_ wx/C_                                                                                                     ``                  __                            4tiL_   J$mmmmWd$$$/L    
                         4447TN\Y   TT  __  aammwm/F    `I.wWCC -____W/$\\             4                                                                                                         +  avk    v/             +        7$mL__ 4A4IP__j4$$Kk    
                          1$$L____ J  __.__JdfRMPPF__  _apmnhkKKC.__jL  MNkkm        __                                                                                                             ff     ff             `         71$q|   4$L__g4$/F     
                          T$$mmwwwW __yxrny____$T__y/K_W4PF_____gmp$$kk /F   +      44x                                                                                                             ``     `                          Nj|L   j$mmmm$FF     
                          4fff$UWK____/`1VZ__../__J/KhW/P`_____W4ANMNKKK    `        f$$                                                  ~                                                                                       __  44$kL _J$$4NN7F      
                            T$$/`__uaiL.  qaxrF__y/F  /` ___pmmNNPPR$PF              `$                                                                                                                                          jj    ff$  __j$TR71       
                     ______  j||__jd#+kkuuW41F__JZF ______44MHhK$F                                                                                                                                                                ||m  `TI  j$47K JF       
                    __.x--  `TI.___ZP`` ____$LWd++L ____jym#KFFN7                                                                                                                                                             y  _||41   4 __jfKhy/F       
                     y++#mm  d+wwqmLL__.Z$$2$kWKTF __amd4fFFF                                                                                                                                                                 +  q4|_|    __jJ/K 7F        
                    ____     ```XX$$bpn++mnmfFF _  W4A#HR$LL                       yy                              _____                                                                                      .               `  W4$$$_   wa4/F  /         
                   ymmme._      `T\4$KL_$TPT1L_____/Z$TTN1kk         $            _j|                ___   __$           ____ __                                                                              +                   j$$g|_  d3fFL /`         
                  |1f9R\kL_      ```T\\wm1K4$L wamu4wk-__$1K                      a$$        __             4/ __ y     ________                                                                             `                    j$$L|__ 77`              
                  | TT7R\\L.       `` 7ff1 _j|Wdf$V#PF__J/K                       4fF       ___           __/_   // ___ yxmy      _____________                                                       _                           j$$mmL_y/                
                 ||    `3$kkL          TT __J1K44ZF  __J/Fk                       ``        yvm+         aamwwwWd$$wwwwMMQ$LL________xaxx______ ____                                                                              4$$D$$N/K                
                 ||     77R\kL_      `TT  um/P  f_____J41L                      y       |  W//`_L. W~   Wd#PHNNN9PW  #++wvmmwwaauawwwwwwmqmppxx                                       _    ________     ___  ___                  4$$N4j//                 
                 |      T``A\\L_         ~ffF ____awwdZ$1                          ____ywmWKCCuwmmK   WV/   ________________99####HHPPPNNNMMMkkkmx                                         _______________   ___ ________        W4$$$$ZF                  
                 |     j|   A\xk         7` ___aamd#NNRkL  /                         vwMARPF WW#PF    _______....uuuuuwu....2_``TTTTT    7fPPNNNXK                                      ____ygwgg________p   wmmwwv kwxx-         4$$R4$C___               
                 __    j|    7\\L        ___aam4ANN$FPP5k                        a WdMPP`$        _____.uawwwm#++~~~~##~+++mmme          ```_____    +        $                         WwwddM$$$wwwmmmwmmLL_2P` @+  @f$\L___     4$$Z7R\kx_               
                 |.    3$     `$\L      \yvm+#f$1N4$KL                     \     4+W4T        _____.aam####PP```````````````R1\L           wwaeL____        w+++                        /NNNMMHMMNMRNNNMNNNmkkwL____  4 kqmp_    J4$$$T``Mmkk              
                 41    J$      4$|L      ff`` 7T  7f\y/  .                 4|    `           ___.ww##fF``` ________________ ``   ____       ffAhmxe__                                _    `TTTTT1NTPPPPPPPPPRN$WwwmmkP~~X44kkL   jj$$$1  @9Nk              
                 `| _ J/        $$k            __y _j|__y/           _     j$                uamm##```________....aau......___   \x..___     _`7f\\mL                        ___   _ui _________________      TPP##fKC __`5$$L   |4$$$L__y/F               
                   ..//         ff\__      +    4/__J|LJ/F          \v     41               WWffT`_____aawwwammmyww#mmmmwwwwwL___ Xhmxu ____   _`7AAmkk                   ___|px/AwwM___aawwwwmwwwwuu...______    `        7$$   j$$$$NNv//                
                   jyfC  ___    `` jy     ``    j|ujfLy/K           Jf     `                 `` ___uwwwm+KNVfKC_Z___ITN$CZP XhxvL_ `1\kkw-wu.pmm__`74\L                ____axm/1 ___$$.W#####PPPPP~~~~+mwwu..____       tqQ2P+   jj$RNNN/F                 
                   |$$    y       _____         _lVJ$NYK                          +     ___    wammm#PP`` W4$ waxuuwrwd4$KL  `f\\v.__`  WMwmmMNN4mL `$$                __ygd4$FK uawwr~#`` ______________~~++muL____    1m4$F`  W4$$NNN/F                  
                  j|1    q$L      waamkL___     4qj|NN\k                                 w   wwWff#R$C    44|_Wf+kVfF__3$kL   `T1+Ku..__  9##PP ~j|  4$k              _yy4mNPANUWW##F`______...uaaeuu.....__`P\hmu.._____771L   Wd$$N//                    
                  ||     4$kk     WdfRkLWwx/    1N4$L`1L   j|                            MYM    $CZ`       4$k_Z`_____a4PF      `` XXmq___/     _j|  4$               qd4RRKF    ```   w _yymmmWWf|hHmmmnwwx.__7A\kkw      `    W4$$4/                     
                  ||     `$9XhmmmWW``5$VWKK      d4$kk     J1                                   q$$L__     `A\hwwwwwwe#PF _____  ____jjjxv/     yy/   $               dffF _______.wwW~~ _V7RC______7$$$FPA\hmv._`$\kW@/P~      _4$$$F                     
                 44|           1     j3fFF       d41Fk\L   `        /                            3$kL  ___  ``~####PFF``       wAmxC .27fF      dfF  j$               4TF _.wwwwwe##/    q4/K\$uuaxmwd$$L  `7f\kv._  W4FF       d4$$/                      
                  4$      ___        47T         d71L      `          _                         ``T$Mkkww .____``````     ~   ```55~~~~``$.   Wd4PF  4$               j$ wxc~~_``T__     4f$ @++W#fFhd4$k    `7$\mkL  `F       _j4$$C                      
                  4$v    $vy         4$    |     ```                   x                  $$       TT  Mhhmw    .        $C        ```  ye+  3MMPF                    j|_ A\ G.. $       `1\ ZZ___`__2ZPF      47fFk  `        q4Z$$\L                     
                  `1||    1$               |      `    mkW            4$                  f|  `   _      ``   Wm+~wwmm++++++   V      ud/FC W//F                      4$$C`` ~+++++++v   ``\+mmwmwwwm/FF    v/  T$C            jj$R4\L                     
                   `j|_     4$        j    |    _        \   ___                                               ``   ```  ``    `  .. wX4$  W/P                        `$$k   ```````     __```f#####F``     ____3$my           j$1F4$|                     
                    4$|_    jj|      jy|   ||   xv           4$                                   +       _        __ ____   _  wmm+  $$            |                  7$\\                   ``````_______  wv//A$$wwx       _jfF  4\L                    
                    4$$k_   _$$  L_  4$|   ||   j|          qt$                                         wwwwwmmmm uuauuuwmmwwwm# K`                                   jy  \\    1/P\\L     hwmmww   a. wwwmwWdfPF `|          W4$F  4$L                    
                    `f$$kL  y/+ A\v___j    1|   $            j$                                     1    ~~~+NNNMwWw++mW#+####$                                       4$   \\  ~+   Amm  ___``  `   f+  `|| $2ZF  J$          d4$F  4$k                    
                     |TR\kW /    A\\L.___   $   +            f$         xr                                      ```````TTT                                            4$    +\L      f1k    _____________ ww/A$   /          WdfFF  4$L                    
                     |  `\VW      `\Xmmq|L  1                         _ j\                                                                                            j$    ` +w         Mmmmmwuu    aaamm#K $$x              J$1   4$k                    
                     ||  `1R\\      `1\4$LW                   ____      `                                                                                             4$$     `  \        ``1NNMMMmmm###KK`   +               j$  _jJ/                     
                      ||     \|       T3$kk `           $    u4mwmv   nmm                                                                                             df$                     `T1 N1KKTT     `__ xv          j|$  _j//                     
                      1$.     \L       ``\\              |   V/``$       +                                                                                             $$                                    wmm//`          jj$k a4/                      
                      ff$_    j$          j|m/  _                    .   `                                                                             $                 $|                          _        fF             d$$ _j4/                      
                      `1$$e   j|k        d4$|   ..                   +          x                                                                     4+              v  4$                        __..                     W4$KwQJ/F                      
                        f$$   J1          f$$| y++                mW/`\         \                                                                                     +   $                        wmm+                    __JfNam/F                       
                        `\\|_              j$| ``                  \y  r        `                                                    _    4+mm            x               $$                       ```                    __yZ  #/F                        
                         `\\vL__           j||                      $|          y.                                             _     y;   J1                              4$L                                             aamNy//`                         
                          `A\\v__          jj$L              __    J41         W4$                                                  y4$           $          x            j$$                                            WdfRNj/                           
                           ``1\\vL__________j$k           _  ax-    `__         A1                                                 y4/P                                   7$$                                         |  /T` 34/                           
                             ``++\wwuu.wwau.JI            l W7f      axr      . `   $                                             yy/                                                                                l$  _`__j/                            
                               ```~++++HHqmmp    _        +           f\      xy                                           M     j||                                          \                                     ++f   _gjj/                            
                                  `````  T$$L           __            `  j|  `1$             m              _                    4$|              _____                                                            4T`1  44M4$k                            
                                          j$|L   +      uv        +      4vk                                ..        4$         f$$___  _________    _                  __y                                     |1M  $  34$4/L                            
                                          j$$k          ~f        `      71                                ~++                    A\$L________________                  __                                       11   j; _j4/F                             
                                          j$$kL              j|                                             `      $./            `3A\mwwwwwwmmmmwuL_____             _______                                   |     2__a4/F                              
                                          |$$E              w4$    y   _    r                                     mm+              ``Tf######PR#PRhhmmmeL___      ______iipLwmx                                 |    ___am//                               
                                          |T$$               4$    |  y                                          J/``                ``````````````TTPR\kk-   ______wwwammkkNRK                                    y_wa4#/F                                
                                          ||$$|  __.         `$       |                                       .       ___            __             TT71MMkL__paaawmWWN9PPPPFF`                                     jy#/F`                                 
                                          ||| $| wxx                  f                                     y++                  ____..w   __          f$$NwavwWdfRNCDN7TF`                                       __jJ/                                    
                                           || $$VUf$L                _|$Nx                                  /   __     +m          ww+r    ..         II  WH9$KNTPF    ~                                          _jy/                                     
                                           |  H4|         +          qy        y                              _   xx    $$k          `_   v++        wx/   TT1P~+      `  __      _                              qj4//                                     
                                           |   3l__       `    _     j|L                               jy      zp/ \\     ~      ____ y   ``         /``    j$ ``          41     $.                             jj$/                                      
                                           |    $mvg L         yy    J|                      __. wx/ __2     wmmF        __      xiL.J/      w++ W X        7     4IL____  f     wmm      _|                    _j4/F                                      
                                           ||    j$F yy        41    4$$          4           wm+    yx/     `T`     y           AAmm/   Wmm /`     xx     //     ~+       _______f       44y           _       _j7/                                       
                                           ||    j$_____        |    3$$           _        WV/`  _ 3XKC             I            ``1    ______     ``                __;    yx-u.        `$|          wx:    __44/F                                       
                                           ||    4$waae_  __    |     Z|           __             yy/`                _______   __ _________________                   v-    t|@~+         j$y         4f+    _a4/F                                        
                                           ||      JfA$LL  y    yy    $$_          ax             y/    \      ________xwwwwmk  +kwwwwwwwwwmmmmxx ___    ____________  j|L  44k___      4  j$$k         ``   _j4//                                         
                                           ||      4T`$|__y/   _||    4$yk         j$k     __     ZC     _______aaa..ww+~~~   __`          ``1N$$ kxx   _yxxuuxwwmxu.__2  _  `\\xv ___  ___d4Ak             _j34/                                          
                                        ___j1      `1 4$ggZLL  w4.    3$|L     4.  2$      vx    yy wwmu.aawwwww##++KKLLCCIIL__.._____________  vvN      4MMM#PRNN#h+wwmKCL_____    W. __../fR              qj4/F                                          
                                     ______.          d$mmkk    frk   `$$L      +  4$y     /     |||  +++H+###PP```T1\mmwmg+wwwmmwwwmwwwmwuu..__________________________ ++wwx_____  tLwwmmy/             __j4$/                                           
                                  ______aapp           4f$L__L  `      j$k         A4xL          j$.  `````T``       7fRKKCL_2```PN#######Hmmmmwwwwauuu..LL..............``__jja..._ A+W/`$$/              434/                                            
                               _____.aaddf$k           _$$$mg____   _. J$|          3$L          44|    __           ```5\+mme______`` ``````PP########++mmm++++++++++++~   .23mmkmkLZZIL_J/L           __gj4/F                                            
                              __yaaamMMNN$1L           44 N$$$yy_   myWw4$           $\_         `$$L.     __            ``1N$mmmeL_____         ``````TTT`````TTT`````II Wamd#PPPP+++-ewm4F        ___ y44$$/                                             
                             __ydffKN1NN4$1L            1  4$N$LL   `|  3$k  \       A\\W         `1+mwwmk              _    T9RNNkmmmwwe_   x __ ______    _____      aipWWTTT`  ``````37PF         yy4/Aj$/F                                             
                           ___y44T1N1NNN4$1L               7TN4$LL  _iL  `$UJk     x   X\iL        ```    Wmm   _     +  _   ````TRR9MNNmkWW4$kwmwwmmww     u..Z2l_ wwWdmKK ``          y/         _|JpKKQ2/F                                              
                          __y44$$1P 1 T_4$|L                  f$$L___jkL   +       A\   A+kv               `    .      1XxL         7TPPf1K 9#NNNNNR1k~~WmmMM+hwmmwwMM###1  __$//      y/       __yammP_jy/F                                               
                         __dd4$P$1______j$|k                  `7$kLW.A$kL_``         \  ``1\                   v+       `1kmyg______               `       441P P###+P`   __$J//     _j/     ___yw/MPF_jy/F                                                
                        _y/44$$$$1___  _4$|L       .      \    7`$VmtL__             3$     \$vL               `   vm      N$mkuuu._________________________       `_      a//`      aZC   ___iwd#P __yJ/F                                                 
                      __y// T$$ 41Nm4___4$|L              `       T7A_______         ``      f+hvm+           _____           NHMmmmwuaeL__g;  x-___.-  _____________  pwW4/``       4+k___wwmm#P`___y//F                                                  
                     __y//   1$ 41N ____4$|L                      4C2$$k_____                `               +mx   ____        ```1NMM#mkWmmkk@@hwammpK _ggmwwwaapwwwmwDNN           `$\wwW##PF`___ua//F                                                   
                    __y/1    4$__1    _d4$|L                      ~+md$$kk_y___..         _   _________      ``1\kwmmx.            TTT$7PN9$FKFWWMM$$kkwwmMNWWMMMMkNNPP             jyvm##K```   wWd/FF                                                    
                   __y41     4$$$1   ___4$kL           .   w+       TA$rF jj|_ +-     _          _ y                N9k              -+  `7T``  WT77PFUV#PPN#PPPTTPPFF    ___ $V    37/F``    wWWQ9PF`                                                     
                  __y/11      1111   ___4$kL       +       ``       _2I|  44$L___    Lu.__i       jZ              ..                 `T   41      ```   `TT7T             44e4+    jyT`   wm4AK_$$/F                                                       
                 __y4fFF __   4$_______d4$kk                        wq$_  d4$kL____  wmmwmmk  ___gxy     ___      ++r   .                 f1$1 _____       __             2# ``    JIC_  /#7P _jy/F                                                        
                __y4fFF  4    41   ____d4$L                    _     4$kL_J7fFNkeL__ ```N9RkkWqy.A4|   __.        ``                           44wmmMwmWw $     __     wmm        _j|$Wv/_  __yJ/F                                                         
               __J/$$L    A    1|___44_N4|L          `         .     `1hhq__T NN4kk_____ ``\ NMtKN$$k  axr             ``_                  `   ~~~$P#+K  $k~~  wvm A++ $$$       44$___   __ax/F                                                          
             __yy/A$$kk   _    j|__414_N41L                    +        T44yr  77\hqLL_.     Wd$kWjfL W4fF       __       /                       7   `   /     +++ ``  ++  ___  d2$$$.. __yV/PF                                                           
            __y44$$P1F  ___    41|_____d41L                _             T4$L____ N4kkyy____  /P_______`$        u..         \;           +                     `$      ``      y++_yyrK__ax/F`                                                            
           __y/f$$PF____ u4_    1$__mwmd$1L               qy              44kL.w  771N$LL__.__   _aaai.w     _  WAt;   X44       j        `$       y             +     ___  _______3/TC_ y/PF                                                              
          __y4fPNI$L_a-  N$L    44mmNNH#R1k               41k             ff$HtL______$L_ymm--  ++++#++K ___  x/ `7         ___  $  ___    yxm     J            _`    _ xx  ..._jyy/A\ _____                                                               
         __J4$1P $$wWP1L H+++   Jf+PPPTTT1                3IL                T$mmmwL_AA4VWZO1KL_``ZIZ`1   xv__    `         xy       ..    7/     j/                  vr`   ++__yzK__  qq.._                                                               
        _yyff$LL ZP___    TT   __Z`     _|L        x_                         7fPHhkKC29fKNxL_    ~+-___ `1\$L_             3$k   __ ~+v                    _         |     `` 44$$wx/ _jjiL_                                                              
       _yy41P1hj____l.         wae;    _j|k        4\     .     _             T` $7P1WWZ___jyk____``5xxk __3mmm   __        2Z    y  `             _____.   ..              ___f$9V#F  WJ$$LL_                                                             
      _y44$FP 5I$LWwmr  _lL____ 4$|L   _j|L         \k  __~     x                ++   4$L__21Fwje_______ wW/f$\   yy    _  XX\    y+   __       __  xxww-  ___       _______yaa.ZZ`T   W4$$$LL_                                                            
     _y44$$LL_j+PKWN$1   +  uai  $$L   _j$L       .   \\vC     41                `1   N$$km4C__JAkLL_...___\______j|        _         \y         wypXMV``__ $          .  yy/AffKL     j$$$$$kL_                                                           
    _y4f$P$KLW4T____j|_______j|_W44LL  d4$k       x-   `fts.       Y                + W41NN$$kW/`5+hmmm~__..___ Wa$k __          __  _y+ _      A4VP`    .y/+ ____________J$$P7T\\Y   _j$$N$N$LL__                                                         
 ___yJ4$$Z$1k  1    41L  qj_ N1LW74\L  d4$LL      `\      ++m                ``    T   `1 4fMNKL_ZIN7PRLLzp_jtLL_2j\  _/_         .  ..` v ___..``1     wm+    xq.  _...aamAAKL..A\   jJ$$N$N4$kL_                                                         
___Wd/$$1Ht$LL_  _1 j|_ _N$kk_j1 _$$kL w4$LL              ``\Xk  ____                    .JfN1MNhmmKCL_WXKCL2g+ypCZL__y______.____+ uy+ _3$kwvr _  __    _______j___jrndVfPFDNk+ `   _j|$FNZNN$$kLL_                                                       
wamdf$$TT  jjp_ ________ 441  J1  V4$L  d$|L                ``  W4k .                   ++      Tf1Name__5\xKN$MPh+mwvA\uzwwy__j./_LV/1_y________.  y___________3$wW/CDJ/F   ZC`     j4$$$$$NNN$NkL__                                                      
/KK$11______$1L___  J$L__    ______N$$L  4$L                     fAme          Nj|      ``         Vd$$kwWZ1__~+KUI1NNNNYHNNlLWj|k_y/____LL.. waxr____ uaxpwwwam####FkWfCL  ___     _J4$FNN4F_N$N$kkL___                                                   
F _J$$$umww44$L _____+hjL__ _j+ ____4+k W4$LL                       \   `       41           _      7PPH9MKua.C__VgF___JTNMM+WW4$LW4kkq..kggc_WJ$LLyxwWWdfKUNMMPFF``\IIL     ..     W4$$$NN1LLNfNNNkkL______                                               
  44P11N1NN444kNN4w441N41k   J1NN4LW7I$_WJ$kk                            q_     `___   \x   wwv    7   $7PPH+tbW4KCLL__J+HfCCPH~+~~~ NammKA4k-___wWdANWMNNkk#fTTL   jamKL   gr~     j4$$N1NNNNNTNTNNkkkqq______                                            
_j|1   __  ____ _____  j$L _ _________$iWJAKLL                   m  __   Nx ___  ax-   `+   ~9f  _     7f  771Hff9++mmmZL____ _`II ___ZZlL22$LLW4MAKPM#P~f$TF  ___  2ZP1LL  $T     _j|$$__LJNNjLN_N$$V@Hmmee________                                       
WJ$1  ___  ___  ________| ______  A4VWAhmYFN\k                    \mw    `\\wwx  `1\    `    ``  ..    `          `T9MRKLuwmmLuaamwwuwmmmwwwmmH#PPT1\VTT       4$vk___T  +kW`      _4$$$___  N$LN_NFAKW77ANmkkp______________                              
NfZ_  _41  _4LL wqqiL____L__i_NlL__j1LZZN$L_A\kL                    ++      ~++              .  Jt;   __ ______a.    TT ++Hf$hW++FP++#PPf1V7TTT`    J N1  ____ 7f+KU.ZL  ` __     _jj$$NNNLL  41L____Dk  `7f$Nkkkwwe____________________                   
```

![Mona Lisa](https://github.com/awentzonline/deepascii/raw/master/examples/images/monalisa.jpg)
```
Predicting...
5$..`` jrF~s; G7bxZ_ _~~j$@|L3$F`Z`SWTPL_.7` .wyrnIC../05Q\W4CW````~````````2|P1bY``````PP``7FF--~~``-``````F``T```@~~~~~~F``F`````````7````F`````````````````T`` `___ ~~`` ZL``55```Y```__```````````
.3sto _ZIL@3s.gtE3\L......A.@-AbYn--#Xhya.L.3\#/APAqyroYd#1#`+----C`G.u`____siL.y`ks...-``.a-T```_..``.`..``S.``@3.F`9--GTG.3SS.w--...V`1WdTNGk---.---- ...o.ux.__~\........eE.csp--~~\u..-L..____.  W
+P``L..e- W41ho$E@@@mgc~dtB\C`C3;U````5fFop---G`_``3IERTF`~-``CCD3LL~~L.s...8jH3rLWz~cd`\.c``\..oaovoor~~+~~~+~`S3cL..```~~+~~~~@`Fq~oiQ.Q~~Qt```5;P`5`.g~~~~_`\a.P~~~~cc@~~SP~9@P`N.``~~~Qa+uoouarp ~
````gs;__W.3|DW8\L..SC5.dwGuxo---W...WdTM7PRSEH\...d$P`\\``..~~;~++-`.ee~~~```V7rL~``5s~~o.---ooz~0`bMTK```````W@6~om+nu..`````T``-3TP+~~~````k --:uvrosCQ.``...ctL``7`5S-`@25`Z`L.q:L```.38`P`~X01LW`
s._o.A-q.g-uicG7FWvw4kdsc09P~8TP\azsbW/`V``_~~G3zhs0lLLJDD~~n.ST``TP~~GTFFK..JXfLL.`.~`.``o.```~`___.z;........`T``````0tb~~ .o--`Q2/```_.___ZL.`Q|W`6@~~~~~g~~~So-oo/G-``~~-..v:o-~iL.e--`j.``````~ ~
so-`T0\qtC@39F~j;_``5fW`FH7```` ~~~~~o....`..`33`P`~~eoxc```k~r\\v:0.@`````~oxqf;--o.`\...~\...F----oowwwymmo~-W...o--_``88.qyP``WXcL.--ae------os..`sG.K`D...-@38`P``````.55Rr8\0.8\G.8``\9--`..---.`
R`c`___`|k~``CG7ou---.````I~-.```````sso:~~XXG33`````67`L.L_S`lL.:b.ox``` ``7`H|..G8s.`~z~`~r~~C.````P`\\.08P`..~~s8`G..o~~~s.L.```~o;n`dt..`$5T@otL__~~uos~~``-o~-_` s...g~``8`@_y@.~~s.L.Z`L~~~``8 W
0$kWow.o/K`Fsg~fY/`88s. ...``\.`..___g~~sv/Q.P~+6V`NTR`o------~~~~`\.8.__..```U1r~of~~o-s..Z```_sL..```.~~s.-o.o````~~oo-`G@arF ....``__`G+--..`~``\...``2o.L...QZ_.._joosC.L@iso.-----o+n;~o..``_.``W
B.`~~9|M|h-uf6RMIL`-#9;uwV`__`\o+----.```~~sr```\c_y/Cq.````TQTZ`.````\....`.`W`S\.```389~~~-u.o+k~~s.-``.z``-:~_..`..```9-`8`L``soo.`q.W7TH.L..`__go~-..sz~~-o.q.gs;u403o9--`--~`s2L0W8CGZL9o\..a.` W
F~---3xM/N1MA@PH+K``07---4....P``08ssoW```.___ ``so/A\G---~..uso--.```qo+---X.qjP~+-_-~~```               _  ``..--_q;.____```___`~~~~s..``3iL..__.d3ZL.@jsL.._~jrF3+-`~G33lL``.  ----Gtcd+-```~~~+h  
F` yW#`N$M/N`$LP`L.sJA```@s~~s:..~~oz~`\.os--u.ae~~`````LL.F~_`___\s..37C````j;````    ________LLLL..L__________   .--o---..o.Q......-q+s.W`FFcoo--P~~sooxoooo-`4|W``.. ~+3;q.n: ``S``H`iE`````.```  W
   /``../~`.`3.``~~~``~-_`3 Gq.mr``@`G.u@@`#@@+A..`. `---+;L....---o--``bo. `9+o  ______...----------------....______` `@0~+h+or~~~~.`G7F~-8C5SbdZC```3g@jyg|s;WQ.L.sg:.``3\o.P\u.or `G3@Es___s----  W
.L .uav/`.._``-````````GG@P~~d;B. .@.P~~`-.3..`0\vX...````\brn~~~XC.`...88L  `` ____.a-em~n#fKNTTTTTTTP2P5~~~~mm--..____ `````8:_______iE3IF~~~`G-eo-ue6G3.oi---~+~33br-~-Q|#|L`~~;` `36TG----`````  W
F~ AV#\L.ss__....a....sc@s.``7T-- ss/C``.b;P+~~ `_`~~  `.``jC`````q+~~-.``L  ____.amd##FP``7TPMTFHMMN+m--CCZZZ7PPhhmx-.___   ro\o..4\.`-~~+6T`````RkW``~~~+@`````S@P``````M/K`- ``IL.`````PF~os.   - W
C``````.wygov+-_@9+Fhr~``~+  `l8.W`#--sswv/``.W`---``L.~--3.F _..``TF```   ___.axdfPTTT`   /- `TT7P``TNTNthmmmiCZZ7P9hmxc..__ .`htcss..````\i. -````~ `.W`F`````.3#F``_.n.2$L.`  `T~~```..`  s3:----  
.  -`.zsQ\m@XG.DZ0Z.D...``` .ss..V.```3-0.  `~~`9@--oxr`` d+L _/___`L..  ___..W/fT`___.L___|  _ _...    7ZTTP9+hmmCCZ77Nhmx.__  `\--~~s.. .g+__S.n..`_yroxF``  ._``\L.x-n~v-~~-...`F-.......o37F````` 
; _GyX`@#f#f#M+K~~~~~r~:L_._syecc~s...``~` `...````.Y`\j. ``  XCG --vr~ __jyzdRC__uuamFWWwuwmwuLuwm_____  2ZZZT7TPbpw__77Ph\L.__ `-_``2; _sd$---:Qo. W2L``L ..qs.``\r~`. ``````-___`_q.F`-3rF3``   `  
LW o/0\v```f#`````\.`` \o.---T`` .a-otb. .w.s-o.` _.`. j;  ...5.W```Y  __ya/$DDwNe#+P-~P~~~+++++++A44mmmuzntumcr`57PNKKCZ77DhkL._ ...-o`----+#f``~3s.X+q~~--~-u3r  `` `.s.` ..j...-...tL@@Q.Ks.. -..  
L __|_``` `` ` __/0|`  @~f```\S.k/``bwv-8.0:``~`...\.o.4\ vrnv----    __yd4PP-~~_`````  .``````````55$91___ZZ55$uZZNZ@5;wdJ77A\LL__ f`7`.``````  `3+-`TRTF@33.P+`  `..~+o. __.z;q;yr~qs---s.uziL q;   
k_oa-o.xc.L..```4-Q.__ .7m----A#/Fss./``~~``....n:o~``Wj| `|P`````.  __y4mPKCSS------  .~~              44. q7P+HCCg$F-PP+NTW7A\\L.   `\.  v.``_.```````T-```~```.cuzs`A3.k--XC@ox..`37``Wtcus1k q.   
.WY#1k@jvwqxc _y``~\  v/dI````07F@-+-....  `~-~`0i.`` `j; `iL.   ~  __jd$PFF~~~``````````` ` `````````   ~~5$TPTZZa4lU$LLZ21VW77$\L_  .-\L ~~ ..-_.` `4V``````  .rbV+--~~~ Y``~FP39kW3tL  fhr``  N1W  
 ```.G.XC@N|K.u...`\V/```+-----`s.```.qyk....`` jrF ` `\c./4k     ___.4$PF````        ``        -.   `      T1   Z29HHrhueZ_|A477$\L.  .A--`..rKGo.  ``       _.._``C.. ``.`````````.3$---`Q\~w. ``   
_   `V``\ AlQ;~+y~ _+~-````````-~~ vWXQTF```s. .7` _.. `$--``L   __uqr#fFF    `  `    .   ``    `` ___         q2ZZZPT$VH$PNCDAXU34\L   ___ xo.   ______  .._...-\.g~~    --  ----3-w---````````   `3 
.. ```` ` `|s:``I  ``.` ._.  _```` /```+ ``..  ss -uo; `7\. `  ___ Wd$$$L  `  `    .. i.     _____...  ``J     ntqqEL_2.p1PDtV`5VZ34\L______@z;__...-G-- qj.ury`0//```  W.`` ``-````````s..vj-`     3 
__   j\.  W--\_yis.__.._~o-   v ___   ``  -q;.__   Wj_ j;nrK   _y/_ JI41k       ./wyr +:  `  --.axortL_  /`    7+ jqjpniu|hWZAWH4V74\L  as--_`-Luxmg6YA  jyr \.. `._s.`-uxv   ``  `.   -o;c`j.    _.  
.LL..______```\/Aj;. \; `X\ ____....   r  `@1b.... -G.W4+M1P  _y/jyWd$$FK\ _____j. /1 `\.   ``~+``90 ---``  ``    T4lZP_____1HqZANV74|W Nj|L..___Q7F@`  WV/L jiL ~-oxr ```\ ``.  `y  / ```ygj|.  .n-P 
~~g__qx--....waiQ3\L_`\___ ____jyjy _  .   ``##+-o-W#+P````   W/qV/A$3$L `\k.oWvG: `   `\     ``   Y````___        d$$__.4wj|p 4ZnYN3\L  JiLz:C..mcF`___y/A WJ$;W`Q7``   ...  \. .4kX .``..ojxr   ``__
_ G--HlkWaic~~~+~R$L_  \.....wvd/QlLs.____  ````` ```| `.    W/AW4|Wd4$L   ~~~~~``     ``  ______...    .._______  ZJ1hurdNqiL_n1H1Vd$LL d$Lg@~++AvL ..y/``.q.$:L__``..  .o---o\u~~ ujx .diy/s.__.__..
-c2ZCU++Wd$L__```@axkkuo:qyg/0\~qjywecL....____ `.  j;      _j. dtLLJ3$L     ______     `_____________________     qZZ2J$UWN$LW 1UjVN4|L G3iK.____jb~wv/CLywqrP\L... ~-.do````8.P`` WJ$bwdsMavwuxwuwmm
$kvw-/`IV`9ho.A\oWP1b~W@`5Y``-___4___$gm+kuug_._ -_.J;      qJr dA$Vw4$L_____.LL..L..    __ggspwwwww.....____.p    $ee-Z$.L2J|LLJVd1N4|Lwe/Fh;L....\.23$LV__JlLLWzs;  4P~~`\.`~`  _-~~yrHy~~~`\V3WW/RC
$MKK6SWw.KIQ/K__XC..```GW@|psFW4..$.W4KQ1NNVhjyp .W/j|   .  W4. _`3TPj$kkwgeeecz__sxcp   qyammeccczzzzzpnmmmmmkW-  7TElPP++HdlkW+wH+Wd$kW+CC/lbgmsrn+_j-RX\.2Ar__$Q;L ```` qs .    .___`_Z` ..WxPFK` .
$KCbxKKD1NyV`L..qjrK__./XNYP@hWzznjVM`Qjr __N41L | ______j  W4\y..`ZLq$kWX46FFGmmmDAVP   dddfRFFFwwmmmmR4NN#PPF``    jET`T7_d$$PP MQV`4|L`5zaGxZE2LL$2ZL_`9Xd$$kW.R\L   oxc3$e-u .uoo.-W4e.ujsd8T` |x 
ZLWYKFWV`QIE Wj6U7Fkwve;WdfK  _jILJl``WJL qqy/|L  __yx.._.   `lzzrH$Vd|L 3fK`@@PP9FR\L  WJ$PTF```7TPPPP5zfF```   ____$$L__p4$PD|L2AHi_4|k jg_jfFF--k-#j\u./Q5P~hq:L`L   7`~7+``y  `ttt; `+-W3--`  W/3 
LLV/L dtL@+F Q$VW/` jj$L.2l___jymm/A_gg/L_jaYC`._  d/A\ku;L  J/4$FW7$Q|L ``` W4T77F``L  dTT`$    W`TT47PF`        __2Z$LuJMfZ$j|n;_d1mq|L IL.2T7`71K`U2lbYK3ZL``4\Lu.L_ ``.`` .._../+---```W2ZL$.  _js
$EFF  ~~W2IL__jfQ$L_.3/Gr_ys.LJ/CELWaaE.L.W31hx:L_WdTP`\MiLwz/`R$.W$$4|L `` ~~~f``  7k  Jf$9//``~~~~~~~```      _~aqd$$PP|FHa4JwVeL_`W4|kwm++n__________9l_______$L@+k    x...swwmm/```_ ` 3$-P++``32/
$EKLL..`Wsskwa.kM+kyg_2J$D/A\W/A\---f5j+m+W`$V`\V.u21L 23$hV/ __jrK474|L      ``   zf  W``T``    `````            44$7A1O1Wq_j+NY|L WW3$LW2ZlLas.L.L-.G2ZLWa$..wax-#PLL____---`````_  _.. j7`C```_Wg/`
PF _gs;..ZE3s2:L.__`Ajrp~~`57X$L./___27IL.W2lKW@g@yj|W_d7`N|L .W71U9N4$L    .  ;  ye    | s._        ~;  .      ___jjZQjY___44WN||L_pWd4|F____@9+~+#####A@@##+nNM4NN4mmwww.2``l.......J:L.2..xws/ XI$_
FF_jywmmm-Fwmjmmmvp-W4fRTCWW/0+h+Kua-neqcppd$;WXGQZAiL____W|kwWdf$___3$LL   :.   jI2   q..$ss.  ```` ``    _q.    4$J1Wj+ku.A\W44|K4DWM41L_.._ZZ__________________~~~~~~Y~~~  ~____ssgg___y+-`Aj.___j.
L WVTN$$DK_`TQPRQ|KLWJtL____\V`7TWWf1U$HmWeA#.U`VX\VAksu.W4CL.|_yvKqad$$k   ~~~` j|y   _____jyp  s.        ___   dd4ZOJNCLg;___j|CNJ|__N\kwspd4bw---- a.w.----.....__``  C.___.G-../qjG$...____ji...gg
;L /F_j3ZL..A4/A3lL--`\_---.__yg|  `\J|P`5~F5$__``_ `@@9;WJ$bmKM2PhjfH4$LL  ``  WXi._____.__jiL  ~~ ``  `  `4.._J$ZZ$VccqJA-__\4.k:q$L_UA\W$FF#9#1KQLggtt#YMNtgqmn-urn___ywywvgqj+KKy2#thbp-uawwykWd6C
|k_|u427Pqycy2`WJ+kW.Kq.W9Ahvq|Q.L  qj;_ 7TWW4L___..Ld7F-pqjPrhYqLWATU3$LL       ~A\u..aammmmrk ```  `` o+oaaawuq_ 47Z5WWT#|KV4t;pTR1NNV`\VpTW2ZB/N\uvwkZE@LV$C7TR1PKh..______CW7CLWz;R$GiLWW4#Q$KP`tg
L_jlWjfKNMAbYK _JT j;Luib.`7_Ntm:___j7lk.d_gzsb-tgp:w~/NTFRlCL.-jYKM1Mf4|L   ee  ```~~+MMPPPPFL___..   `4`P```  `$ZZZCZZR1UrN|PA\V1MI|N|Wj|P+W~+#-W4#+@@+H-wy++qC2Z$LVtbpmuaaeWdAkwn+FH|N9F__`$Xek_2s.
LWv/KQTLW7#M1kwxR\.JFuziy;W4.U4#-L .d/Cb;xee-/`5ymElLZ__g.WjymKW7TPh~NTN$LL  X ______`7_________.pmk~ ```~__.  __jqZZq$KwWMAU___j|LJm1N|WJ|L  3Tk._`$`STP`XO7CIW;wymWd6@P~H9#hVP`5WUIC____C..2/#Yh@eei
kWfCWv+LjfKC1WJ/hj~__W@mYLy.~V``\h___`Sg._~SSZ___F5+y-uae-W3TR\V|`___j:M4\L_   wax---......aaaa--PFF    _________Z41nj4CWfPW4:kW4|k_OAN|k4ikp-#thtzns.D1L_./_vWHTP7PP`RTC``````L.  ___ua-wvrnyF2|KZQZA
KQ|kWf$WJAK____L_J`NV#P8IL.c__...Lwa.uzziL_@gyke--3lB$R##PWj;N4\.r ax/CL3$LL___ 7``f~~~~~~~ffffT5L_      ..4|   41___2q$zK__j~_VJ$VN7PN1WJ$kK ``Uz:@zr__u---_J$``K\.` `` _______ss...kWffKZCDZ-NvkW4CF
___ `jamrF`\.L-ees_______~j:.g-+~ssz+vwmik-##2R5F~gjyrK`` qJr_`\lL_dt$FWdA\kL___     wGGww77T     -   ______|    _jaa4q|K_..____gJtdlLN|W/`\VW _gg_W/#kW.f$__q.._.g; s..._.__..Gaarp~cq$p+q~~~9M|K``\_
kZ|W.W7R\L qiL@9F9x--w4eFWxmsWSZ@zFEZ__3$K8htrFRmW7TILLuimW4O --4+WZ$$W7Z79\hkL___  PP#####PP\\V`~~ ______aa: ____dfMWUIuJdtuaW4hf$jAWW4Kk.2.L aa4$PA##n~~qy/wywveu..qzpyqsuva@@@MFK7wMTC````___`  d$W
hhipWN.Z$x-d+K_Z`2Z`5f#f_j$ELgsg__E3ss.g|__~j;______~-____`j|L_`7$$;#1hYKUZ75$kmLL__ ```````   ________app#A\L_.qjptPNM|gf9+Wfq|FTQZDUU$rj~ggL ~99tKV`````u/KQIDN9Rq~d@D@P+H@@@__4L.__2lL._._uxg.p@n+W
|N$KLurWymWUIKKCLpy- y/`war#mE###--d7kcpiL..2iL.....ZILZ..WJ$._..d7Z___| ~jiQ7PNhmcL____  _________--apmk_____uaa$FFCd$$p4Z__|N+L_jgp N4lL_jyk- 77`_______/`W4+F TN$TP~sC``E3ILg..~~uaxmkwzzLzsq;K_Llu
kU$AW/LU|NykrH@hyM1LUlL WdfPTPRI5tCW_GSPkko~d+H@@+++++H+++-H\|u+PHAL.-___ 2lJ$LZ7N\kL______....aavmyA_____aaamMPPfKH1W4+Pntwu/U\Lu$4L.N$$KwjYKL@____.L..... _`|L____|______~y+#g-- `W441N@+Aeee3:L.a-W
LN$FA;WJrD/FILJQ1KL_.Au.____``FwdmcuadRlLzWW2ZELZZZZZIZ`TT``J\VAL__jrKNikWaa4cLp7PAFhkwwppgggg__2l__L..a.w+HRQKC_ZlU$PT$CUZDJ\Wg|Htgp;W7I_UJ|L_-__wyrh~njc_ui..L.u.amnwyxK..ZT$CCLL..#zcL`___~FP+h~4T_
PP\KJ1W`|K`GakW/AGvm/W3;b----wVMTF~H~PP+~+--+-F@+++--+- __  d\rF_yWM$.#tLLV7$KWPKN4TNNNMMAMNMwammwaawmmdfNTPN|ww.m+PF   qywyTkWd1NmYn|W4$Wd4$LWJDWMZDN@N4P-H+++mmWdf@UV/|Utcpxdamwumr__~_ss..7``TW q.W
K__Wd\..  Wdf1L``2f5_W2E@ZZCLL_________`Z`W2ZDF7T`5T``LQ$E~ WJ1LUJ+HnrKFwv;P`I5$PWf+HWMN|PPNfMMRNHMPNPPP1R1_d1N+PP``   qnIOJKUdjKUJlU1NjtMd#+FF++~~~~p####_K`777`NjF#aKC.W`FR;5ZILU$L..22@@ss;LaxcwyxW
k4vwyyXn.WWd$$k__j$wmvwF------am--yg--eg~~~~~~;   zc5.ua+F` WdA\q|$IDP  M1h__ZJPF__T`I$3lL `````T7T$V7RTTR1 d1K`1  . __|MlU;hj4ZFH`$P`WU|KCZ|F`7STG77Mmmua.uus...U$MVP~~~nMAGmmmvFw@++n+nEE7R\Lg~~W/`5
_j;LWJDM+_@A4lLLWd$MRbUT`RV#@@P855f###```TF`FS.._yew-+_3IL.___ _jywj|L...ID.ngr___._w$Zd$L       77P+~\o\MmWd.  ~~~ _ Jqj$E__7njCDZj. W44QaaiL_;###fP ~~~~~~~++~~YARKK77`7`#fF~9lKW``CUTDTM8OD+nyy7`qy
.axee+N$CWVP@$h+#+FE5zzszz; ____ g| ______ ` 3$Lu.LF`5-qip~q_. Wj|K7|wynyp~4UZ$Luq4|W4RN4\L  `   ```` --PP`~s:K``  .-W4NTPAkkcQ$$kqqrWWthY44$kVA_____________``_2TP`~~j_..__`_______..z;.`55;``Ul.  j/
V2$EEI2esz:W`TZTR`555FF-mmeswa.csq._q.a....___j____________jxr_Wj|L\1U1U|P_ydtj;Wdj:P4UNM$LL___ ``  --`````T``~~-----`\NtCZ7fhWd#fWj|  \VIDZQ$LLwiepxcpzaaui_..________y-- --W.G---_ywmmr~_j$.wamcL_Jw
mEFFFW~F~~~~~~~_____ZC2ZC5./Wdthwj:udtp+hmxL..4_..-j....4..24\WWJ1kvWM\M|L.wOID$MWH+NmMMPP\ku-c   .`#-8..`~T`  `` ``  W7$\xL.944OTN4|   a;PA#AhYH4#M@@H+++HGmrKC..wua-cZCL.2z5ttVXKODPPTF`wv/KC7$FwW/A
NTF```T````\``W4y/kwa--uyx/````KU7FHd|P`N7AhywcLzd5zamwwqtmv`|WdfF XL qYAhtu++HAN$NDPPFFF``\VA~ __. ``@3s `...-n.     q|7T$kqy__y Wj|LWq$IP 2TN\U|RKQZCZZI23XCLzidWMQDhkua:n--s __yr~CI. WVfC yq$V/P`U
P+L_._L.L.Q.LLL2iL___$DV/FL_.qiW/``N7IL   d9fFhykke@9$KWVTR\L.W7ILw__wdfkUTNTF2NDPPP`````  \.   .......`  --_..3s. ..-`1  _4Qywq.  j|k d71kW3|P`MiP  wwwmwmZFwWdAPPA94BDHRFF`@__jy/`\y/-_ 7jrdIN3rK  Y
``5igqzg~~~+__ggm-u.p/#fC__z~9gg__ Wj$kW/`W4$WWTF5SE73YW`__9+wu/A|PA4VJ1U9$Nwm.PPK``   ..__`\y ~~~+~--~`  ``s:.`~c.z: ____;njfN3iLW3;K 2fE|W31LW7AKL2Z229P___ ``F`TP7FF```E__S.u3+FhW/CL._|JlM$M7FL_uJ
yyd+AHxEZ____yWZOTNXKFk\ywaGW34Gmk_WJ/Nj|Wdf$W/A\V|NMy|N ../`lM|U1L`tY`$V`AM#PF```    --ee..4.. ```````  .  ~~  .--~~ w.wyrd3$W4|kW71h|d$$. 31W+K7hxvw----..L._.   __```__y-wg+d`C_W/\L_wwammW`N|Kjy-W
DTRTP71NS----tQ$kWUI\L_$VWH+P@/##EbV/`_|Wyd4$PFP`\$Z$JFW m+hqrM1H|;uq$LWlKQPF``    `  ``Ts;.~~~       ..    .  J/````WWfQ/AWd|L5|W $|W|j|P1W___I$WMAKCC|`ggmmwu;L__..  am4/KW4$ZL..W`$V4WUARL  q|WJ/K7
K\h\.`F T3M|NWMfFk+F` q+K__`$Z 77F `__u/qiDNTF`W`fNmg|LW|7`Nj$7TN|F_dlVPA$VK`   ``     ```+  ``  ` ...-~    .--``     `\41L N$wy;W yL__JrP\V___yPAJ7PhqiL.`@MRMlL----LL999$k@@#+WXAkW4fPP`_____j;W/CW/
L _g____JJR|WXTTIL`` Wd1PwwaxkWw.L.WayMWM+FH\y.L d7$MkkW| __ym_|U1LudrKCUJ/L        .`  ````  `. .r~~~``   XJ`````\.   `J\y.2JQ$LWd|hYd41LgXuJ#/L_ZlTNN$kp_____@K__ZLEE..2LL.LL.22L.sJ`__`-4.-W7/P\V/A
L`\aa.w-eJD| ``$|k__ wvrhV23$LP~+bWddtPW`` .2rhV`Q72f5\W___J4Qp+HAM/KC5xg;F      `       `..  -  4C ```  - `~``` ----- __3zeu39/L  |Mj|$$Vd$V/R1k 44- 7A\VLL.__A\WyA-@yFnwve~~qymmw~~cL.._gatmW/C._/__
L ~m4CP`jjM|L qy|N\..___  wG7K `TFWW#A\S.kaedTP` W|`F___uxmdONPKN2MCLWYK5|K       ..      ~~ `` ``\.   `````` __. ```W\u.d4FWWf$\W_|_qimw$wM/____________$ywtgc_jy/C@@TCP`XT`77ARKFRGkx+nvW4PPP~9X44--
k ``7\._31M| _jy_Uq\Lu..._ 7`\.W4LD/N`#V|__TP1   J\___yWWffPPK$NN/FAWPA\a;b   .   +--     ``.... .3:`      `` -a..    WtcOA\U5TRtLWlmM1L@2LLLL.wwwwwyww-444M$mmWCZ_k-s:L..LL__``______````5``````07f#W
K___44xWdfRLLWdImWd$kWajc_____~-++c__;Z$$W./CL  __j_WdfPNPT$TWjmRCD2KK@M4FF  _- -````       ~~~-~~~`    . ``   G+- 3 Wd$yK`_Wy__$WW@B9DV#-F++~~c#f5zzz2222$5$@RhhmwcCg~g~+----__j..--..  _.____.g~~___
L--uV/1Nf#hhvWdmmWW``W74\k--..__`T-wxeu2d9fhfK___..a+HTFZL2Z$U41Nkc@@XY/``   ...`    -  ..  G7``.``    o   `` ```_. __23:D\aiZ$W/##FE-zz5$7TFFFF____~~~~~~~___.T71Namu_TTTN7Rkkcgz_@g++__aip--uiL...``
k`#P~` 7`__7~HTR7__.  W4#Mfhmmw._____| `A-CD/__yymmPPPTF-- jjmmKPFFP`55;     z:~ ..```  `  ```                  sv- _.wrcUx/A+-_CL55www y~_____C...ZT7TTT77AvwwzZT7RRNVLD|_/55MkWCwV/Z\wwmwkM4MAk+etcg
L_LCC____4V/``T_\sz/hYWNTRTU`D9kn---s...``F __yV/RZLLJ/K`CLJ4ZRL__   W++ .   `E..~   `       . /       ...      +`  V/Q$FP`CS3$Dw+--~~__``_.-vygggg~sg__tf___|Hj$L_2294bKC. W`TN9\Wd6kzcEE____C```R\.u
kmkwwx/kc...___zg~++WnfZ$5wWv@Z$WWO#mnu;L  __y/f$Iqykc` qqgd$$kcsL._ ```      `s./`_    .     ``          `    ``` W4$~+_SSwvP~~_`C___.agwaddsUN$$7F--4vwmwuxw.71kyw-CZf5\iCL_-W2l5f~j+Fm--.____ __~~V
P|F PR\LqgqipwvcCZ`__2 wa-RM$KGWMtWMODPP___.J/$PP~jTCL. jjTR$FhfhmiL___       ``+  x-  y  .  \.       _..__        _-``$vg+______aaawwmmN_A+F~~~~t_|222LL2|gfh;nTDXCD\K4.J$hiL.hmmwTZZI229h~m-C..___`3
L.L___spwGQvW#fF9sw.--_______@@@_--___`___ua+AN|L_21k+c_j7FQ|EWAW7\bxL._____   `j.`` .N/  . ._    ..  ---..    ____`` _gfC5._yaadpW#PPEE;KZZZZIZZ$axmmnu-wxmwj|Nj;h\V4DPXd$QbL__.DD|hd+w-ZZZ`5~~wxcc_g
h+c.pwm/@99KC``33#c~5`\.....__-`ST`5___yaWdTF 4|uamPK`_WyZLUlkcL___2zhnwv...____y__          ...  z  ```     ___.g__s..`_yaapMANVP_5I5wmmnmmmhrn~+H1NTPNTP1Fh4:LJ;F+~j|K. 9fRKu.n ..W4OT#$~-- 7`Dh\cc_
7$\kL_5S_2P`  ./A\__g_gstr~tss.W/oV/_GV/##PLLWJ$MfPL .wV/AWgmkh WjayF`2Dth~~---uiLL____________          ___..aaasv-____J$#PRCC2$_wyrK4O1UPR$UTF`TN1N\CUWM$|WrAWj|_`W.Z|L.Z`$kU$LwXt.p~ ___4Vg_  ``\bx
_$7hk--A4CC  zc__X4a.WW2PL__aobKGV` uW4fPR\.wWd$$ZLLWd47CU/APT__yWfF5yW/`F``DDX#~mmwv--u......L.__________uizs/4_2;LLww--+S$L__ga4U/PNf#$F__7`|L_|p UJq:L$q|KCDJA1bwn+g+P+KL2ggyKL`\___ q.._tp@.  `$7t
utcL2___25k-_a\x..~~+##X4LWd3KLL2LLudd$FK_J+F`jB;h\y_AM$kW47/`\v/N|_yZKD._qyWKCTZ22DN@@h~~~mmwmwww-----wwg@@___u$v@e~~f$ZZ3JaKNkdW/`_V/h7 WyrL|L_|P`4d6$FwjlL___Mj||NIU5Z1kks55$EkWu\L..zjy_TF#\L .Jf$
M4kwx-.._`___@P~~~`7IL`5~~~~~@@@@--y49PFWW71LW4TFFjYL_J$kuWXC_mtKN$y/+P__Lq:F\g+pyw....Z7TZZZDR@@@#N#X@@VVPP..zW+KC55wmmmmWdfPhfN7K\./A  WWfFW+Hd|k_______2$k.L__q|.__W|g..F++@AKCWWmm~~yA\McLL______t
M`U7P5XiL..2##C____.~L..```____`---3TP$LWJr VrdfFWj1K42LLY`\jy``Wjy/ACLqyzd$k M|yjyprrngjrwjy/q.p.$.LS./A35wv/~KG-WWdfPRCDN1K  _jTNjYK`_j;//N``N_|Lww44-.Wyrh;N.LuJk__jjupK`Z5$PA\..NTC71Mf55bn-----qg
keK4Q7Q\kL@@@pnssvurEEEi..._j.G``WW4TF___fF d|d$LW2lNamkH+L2lLL_W3/PR\bu/FRlL_JnYu/BTTNI7_j7T|N+uizpvWcGSk-_ZC_.Vf$$RTDI$p41C|L..|UJ|L_WyrF`Nlwwm+P-~~55t#fFj1h+mH+Lu.dJTPkweWA\.aiL_  /q$_`3TRQtWYA\M
  `W4tN$kVP--P@@RtU55FFjmpxWdA@9WWW$$DA\41L_ggg___jydQ$K``WamKLWdffKW5WMTF`ywy/M|#+y/qy+jy/qyp/|NWPP|$W/c55wwxe~+P_AVphmTPj|K_yj;_y/__Wd/C__ym+~~T5`T ___``W`\P`T``_yg~R4YFA\Cwq;PA\L   N1F R|_j|W;n3f
____J$9ANYKD$k@FAxeL3$UA@R1NTS7____+fKUJPKq2g;G$.W`TPj|k  _7FhYd2$LLW/Z`\_V/F7Q7/7Q.CV/C.X4U/kpx/C55x/jGwW/NU$CCl__2lL$ZALq.A\V`\W/KWW47A\s./Z```____$$$-`AL2$ _.__.JFPP7\L2J|LJlW`$LL___`__j\Vd|Q|L`T
.b--qdZ$M1kWtNmLUPF--+mQID1K____..2TZhaZC_j$RwMAtbWdNQ1h.Wd7CUwymmrW_|__wv//k_y/k|M+W/rVrn~M6V/```W/6VW/PR$awrnmuupMAmrL__j;D/|V|MKuV4M1LJ#KGwk-KGG--n+#YN@$y___jpaWPA\L__~+M$WH+kW4$ku.__..___d;HiL__
Fhf`5$NtQ1F $P~+~``@7PR44M4NW44vmn#fC@fA--dIPPXP1VmFWd|N|WdfhW4T$PKW|AYg2/``_y/A\WN|N|k4|Wj$kK`__W6$k__I._jMPFN7NfPKO7A|WWZ|KdlNxCuVwy/hWd#1k/K`@WdfC2I.`-_jlL$5wMPPLW4\_W71N4TN|bWMfhhmwMmmW4vH|P1F--
F7  q4Q$PFFWTC7T-  g```2T`\.`~jfC57$$-CClUM4F``4ZIL _j|H`Wd1WW7NI.WV|NtEE;u.W/ANJ+/WU|kjwux/F`_y.__I.GwpmwrKC_uJMTC 7CUlL y/FH+P$$W4O7KUJ$P`\.W_yZ_. -+___4$eW+PPR$L__Vd\Vp JA1U\V/NTQ7|WMfFU#XQlN`BW4
P____jy/F` ``_~`` Y~\______   _|..;22tbz~~dIlLdJ$EELWJ1N WZ1W2$NjrWj|Hj$PFNWM1L/`lLL/CW/P/`5W v+cL.j+d+R1PFL_gpfPAV/`WJAL./CV4ANW4f#7|h~dA_.p;Wqipu-WZI$wWdATKTCIZjrWNtddtLK.P\VLJL__Mj|  `__`~N$kmrW@
_la.uJ/FL   u..`` ```\..G-.`__jipmmc _d$C ge;_~dfFF+Wd|L.q$FHjiUJLWJ1N4$FF `7DY;.`--qhxfK`y/e/Z`kWdJP`TD/`_WjIPL__JCUJKQyrwVrA1|PQ|K`|W/Rqy/P` J+K_|5armHfKD1kpmmNM1LgjTR$Lp\V`+HmmWJ74\L G/K. 31N$LWx
mm++#/`  y  df\V `\ywsg~d|k__yymB$RELW4PL_GSEWT7`TCI_$|p+HILWj|p/kWJ1UZ$FLWJ$V`VWd$$WMPF W/FK`wd49PK` ./__adZLLLuVZhVAQV/CWj|Nq|L-+uyrKC_jfFL__``\aaW#PTNTFH$1L|$LHJhiuTNQlL`\V`TRR\vwd\LW/fh\W``5++W4
jTT`________________________udf$PE_5\VZ$VwH++P+L__wywj|L`7\YWjfP1L2;hj$ZLWjrA|W`9-qjNPK__JTF_W4$VKC. -AC.prP$|hjVFFWIDW/FWW$kWd;K``U/___WdTL_i.._aMfK$$1N|KN7|NrP__j7AH|N41k_~+_____|_7A\L__________`_
_a._a.uuaay_wwaxuw___y.___aWdfFKCS.22F_./67TlLLu.VN1NJ1L.WJ|WJ$CLWy+W3$ELWZIN|L_|AN.P`_../_WW4MfPLp:K`54MMTR4lNJKCZJ$P_|W49fCW71hyx/CL.xcj$uWj+Wdxd$lLNWN|LJNNM|k.wJKC4lLdIL.Z`.a._S-k_7$LL..u.aiu.www
ddfkdthkdf#NM##fU6U4NY:WyzkWdTF`jjtKCFWiEF`~;~~q~+N$Uf$kwu4|K42r__|L df$kWuiv|uaicJfC|WfrNvWUI55$W/|__dJ$N1WjtHtLLqVZ__|wydiLj$LV/R1kW/fKdlVZO$W7A59A$PA\uxPP_Q|ktgj__dtmjrhiuxcpaumtNWfQ$kuwVfRtHfKWd
WdfF4AHfR@@~tCLz__zz5fhyzdIL2lLL.2RQkLd$ELL2ZZZSZI2TF~CUPN4C_N4CLq|L_$$TKLUzK|Wj+FF`\y/CL__$kepv/``L.qjpL__ d$PAV+q|L.q|P/Fj;p$NX|L NVC___j$kMAHA$4TRTL_WffLLwu:nwqlLWdQLJ|N|N|PPj+Fkrd$MTFWPTRUTP1F_j
ZZIL``P\5j-_9+---___Zl9XAh+mH`_y+R$H+F-@A+-----_jy__ `j|__3iLJfhqd:hJZD$hwV/RYKZZT`_J4$kXq./pFP`_.grndTFWu:udrKV`KdlLW91KC$prn_NA-- _j_u.wdfNfKC2ZN1Nwnxn_jpwVfANyH+E__jxy|N$MRKC4TP4$W4IhKCKTMWOKK.W4
wqyg___2WdlWKC``_2SS--df$NIL__.ZT__RIL_`````___23.L.._3$LWjmmnwwq7FWj$P WjfFUjqirL_jrPK`@@fP____arH|_U1LWfhVR1uYCuJ$FW71hnVKCUaV/1L_j4wgrKj$g;pj$CL__|N|NWVN|KCLJ:NIELLJNYKV|P`__tCLgfNl$EDL________W#
_Q$F---ggg;F___.pxWKCCF ~jAL.gg+_uxFn---A....axqz__j+u3;K dTILPWN$KWj|___7___JdfFLWJPC_ W7ZC..pxMCGlmN`LgPR|D|H|LW44|NTNTD1FuqfKK wurdIZ$LprH$VWArnwu.J|__|hVuwW4:H+rhpw91N4.L _44kg;.44HEB;N..4C...__
_4lL`\_qWZZ__.v/____aYK_.JFwxK4$W/AL__________jjmwUI.Wj$L__j_____1_WN|____q_______g/__._____w_______|_______________|________4|______________________|N$__________W_________qL______|___j|__@gyg~rj;wy
```

![A slash](https://github.com/awentzonline/deepascii/raw/master/examples/images/slash0.jpg)
```
        __.._                                                
     __.wf``\._                                              
     ~K$     `\._                                            
      `\v_     `\L_                                          
        `\v_     `\L_                                        
          `\._     `\L_                                      
            `\._     `\L_                                    
             ``\._     `\x_                                  
               ``\._     `\x_                                
                 `~\._     `\x_                              
                   `\x.      `\x_                            
                     `\v_      `\x_                          
                       `\._      `\x_                        
                         `\._      `\x_                      
                           `\._      `\x_                    
                            ``\._      `\x.                  
                              `~\._      `hx.                
                                `~x.       `5x._             
                                  `\x_       ``x._           
                                    `\v_       ``x._         
                                      `\._       ``\._       
                                        `\._       ``\.      
                                         ``\._     _./`      
                                           ``\.___a/`        
                                             `~\e/`          
                                               ``                                            
```

