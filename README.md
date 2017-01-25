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
j$__   jrF~j; N7hx|_ _j~j|M|_U$K`ZZ$WTZ__ /   wyrWIC_J/OJQ|W4|W`5 `  |`\````2|N|NY``````PP`_7F+-P~V``-/`` ~TT`PTKSE ~~Eg~FF AFP``Z```` 7TT7T   __  _`````_`   T`` J___ j~`  lL`255|  Y/``___`  ````` `
y3mxh _ZI @jywg|EA\L_u.wWYA1W-AhYn--#Xhya.L__|W/APAwyrnYd#1#J+--A4T wxw _   41H|y1k .. -_  w4T`T_____T| L.Z`T.  W31F_yTT7TC.Z$S.wvw  xV41Wd1N|k--- u--   ..p.uxk__j\4...ZL z$u.c;p;w jww v4L._____.  W
+PP\\WJA+ W41hw$k@##wkc~d|B\VZC2|U````5yFqy--|K`__`3IERTFP\V KCCNlL ~~Lis.wvdjHjrKWfrnd`\kcf`\L uwwvwnrw++~W++  S2IL2.Z`  ~+~~~;@1kWrn;U/W7;N|P``UfK`5  g~fr___\44PP~~mmc@~~$P~9+R|NVPNN+Xta+kw4var  g
`   gs;__W_N|NW3\KY3$T5WWwCuxmyn+W__ WdTMMPKM#H\V..N|P`\|KW. gj; ++K wee~;V `jV7r  f`5;r~5v  ++mz/N1NM1K7T _`_ Wjywwm+ww.W`````T ` jT7+~ y` N1k  x|w rn Z2Z  4.Wdt|_`7T5hVW225`Z|  q;  `C JZ1PW~XM1kW4
s._ vA|wywwyiLd7KWvw4kWzKQ9P~HTP\uzwkW/_V/`_ +UgzhsdlLLJ1kh;nd$1 `1k KGTFFK WJNfCW    |  X41W`|k ____z;;;u....  j/`_Z$ N|k~   pA-  2/ _______ZLYNQ|W_$_y~~~ gz~h$pxw4/k/P  j+n.ywn y|L y+W`j;    `~  w
g;V/T91h|C2J$F~j__|__|WPAH7C```  ~~~K4__.     33`P`~~+WxK `1k+r\WV|  W/`   ~mxh|; -__ \k  z\...F ---wvwwwywmm+kW4L.w-__j\MD W|K` WXtL.  4ek-4-e;n4|  X4CK`lL.$FW4ZlP~\     J$wr/KU$M1V/4T  J-        `
R|  ____|k+P`CU7wux-_|```jI -C  T``7 Xtu:  XKG3$/K  `67ILL__5`lLz;\Vm4C    77|N||KWk4Lc___jyr~+C. ``PP`\YZNJTR|U~~d#K\..z;  dIL   `F5;W dtLWJ$5TWdt __~+ \xy~` Wj;___  .. g/Kf$ __y_|j|s;L2/$         
D$kWwwvW|K|kygdfV/A$Ni. .jT `\r i ___ jfskK41WA+KV/N|R7 ~----n++~WMNYN        M1r Kfrh  sC2ZC_|_|L . `  +~s/__Y ``2  wtmxT wyrk   __7    j+n-| |  `\...  23ZL.. j| .._jhpxC| JiE3J-y-A|v+nymnx.  _|  W
K/ ~~j|N|h|uf$KN|  +#|wuwM|__|\ +Ky--.TT   yf ``\__y/ q;Z`W2TNTZ`7     L./  V N|$$L   YM#+~~ uvN1k~~ y  `zz` V/  _   J|R`1 X7IL   upx   W7TN|wx ____j~-  s;~__\.j|ks; 4CZ39+-`A-~`\VL2WVCDZLD+\  41  W
F    3|M4N1NAQPN+K  N71HA4\ 44W `UMkhwW1  ____   5z/A\y+-_  :W4y-X    qy/A  Xxu| A+__ ~~`                      .   __;_______y___ ~~~ uiJ` W;L;___.d4ZL__jK_____j|W3+  ~j;31L 4.  ++--Atcd$k``_ ~~+h  
F  yWN|N|M/NN$LP|L.$JAT``5;~~;; .~~qz; | wxxlu.wy~~`  /`LL.  ______s. W7C`   j;| ``    ________LLLLL.L__________   .N+\x-wy.n _|XC.   q+i WJ+krsp#+#++mwuxvwnx- 4|W`CW. j+#;hyn;  j$`THI$E   44  ``  W
   / _  /~   $|K  ~~|   _jy ww;m; `W4Gwu/@ #|W+AT      -++;L...$Www++ `1hy   J+/   _____...----------------....______  _\U#+N|4rn~~~|KN1F+-HC5$WWZC``_$g#jyN|| W4$A sg; `|N|N| \u.zr  5$EE____Xy -    
.  _wyy/`__  |   _`7   4K4P +d;B1  d|P##A  3$K1D\vXr  W7T`\brnf##XKClLW M1L  J  ____.a-wm+n#fKNTTTTTTTN2P5h~~~mm--..____  `  |4;_______ICZIF~ ~4Gxx  ux6G4/Hx-  x+ 31N|  -M|#|  ~~;   36TF-k   | `    
F  WV#1L sg__|L  wv.n.xcH4| `7T    9/C J1hYN|    _        _jC`    q+~~n+ $L  ____.awd##FP``71NM4NHMwN+w--4CZZZ7PPhhmx-.___    n\h.W44W4+~~+N|K 7M4$kW/`~dz/PA1WW`$VPPR| _`M|K|  ``|L. `7`V7P  j|     W
C  ``` Vwygwvwy_+HY+hrA|P    Ml  W #+hyrwy/ $ W| -   L. - 31k   . 4TF``    ___yaxdfKT$$    /   TT7PW71N1NthmmmiCZZ7P#hmxc.__   rhtpzs:NfT``HlL x  |   _jWfF`     ##F`    .2$NW    1k          J|   W  
|  _  XXQ\wVXGlNZZZ1U$ |     5s.KN/`` XCU/     w$@-wwxrj| dfC _/___|\..  ___y.W/fTT___  ___|     _.      TTTP9+hmm.C777Nhmx.__   wv ~~yv   g|__$.w1   yrnxF    __ R1  4rnjv++++  J4F _     .W37KW  U  
; _jyX @#f#f#M+K#/~|yr :_____ye;r___  `|        /` NYf\jy ``  XC   wvr   _jyzdR1__uww$FWWwuwwwwlwwm_____  WZ_ZT7TPhmw__77Ph\L.__  -__` ; _zd$k-/:N$; WZL `L   wjx `\r j| `X````y____ jy   yrF3|       
k  M/ Ky/| f T`   N|K  \ux---T`  yxyy|    wvmxu    |   j|  .  5zW  NY  __yJ/$DNwNe#+P++ ~~~++++++AA444mwu dt+mtr_$7PNKKC`77A\kL._  . +j| +A4|#fF  3spX+k; eH+ uJx      .      j._.a.WJIL__4|KjyL  .   
L __|_ |       ___N|   jjf`W`|$lk/Q| wMwK;Hf  ~  . \y  4| vrwvx+      __yd4#P-~___```   C``````````I5ff1___7Z5$  JANZ@| wvJ77A\LL_    N1 ``5|`    4+r THTFS5wvW+      ~+y| __y2;q;y| /$---s.wy|L  |   
k uaxuaxL L_.   4-Q| _ J#wkvw+A#/F s/  j  `     n;    Wj| 4|P``   .  __y44PKCS4---     r~~              44  _ P+H4__$-- P+N1W7A\\L_    \|  v/ _    ` _|N1    | `   uJe`A4$ WwX4PhxYK 37T W4;uf1k d|   
LWW#1k_jywwv; _ ``~|  v/dIC`2I07Fyy+K  ./    -  QlMw   j|  |L       ___d$PFF ~tf`````  |`     ``` ``        $1    w4lU$LL_2|VW77$\L_   J\L    y  _   44V` `      |hV+-  ~; YK +FP41kWM|L  $hrf|  N1W  
     hV4C N|Kyu.L /1V//  +----   Y/`  qyk       jfF    4|  4k      __.44PF             |         y           1    21HMrhue___A\77$\L_  ;A+   y/KGv    |       _jy  TC.        ``` `| 3$__ `Q|vw  `    
_    V|`\ A1D;H+y  _+   ``$```  ~~ vWWQ1F       J` __  j|  `$    _ wqr#fF        `|             `| __          _  $ZP_|VN|AN|UAXU34\L   _|  x4.   _____   _._. J/  g~~    |      _$ywvA4 `|M| #       
.x   `    _|s; `|       ._   _     /`  |    z  ;/  uj;  |N|    ___ Wj$$$L             ||     ____        J     d1 J$___.p11N|V`_Vd74|L _____Jg;___../G-  qj;w y/N/      W.2   A   7```` s. Njy        
__    \   W7A\_yiy.  . _jy      ___    |   q$___   Wj| j;N|K    y/_ JI41k       v/wyr 4|      uawxmrt    /     7  j$yp4iu|  |  44V74\L  wyr__`\LuxygQYA  jyr j.     s.  Hwv       |    wa;  j|    _.  
.LL. ______```VJAjy  \;  X  ____...    y   41h4ZL  W4$W4rN1    y/jyWd$$F    ____j| /1 `\V     ~+#|N| --4/         14lZP_____|  _ANV74|W Nj|L .___|7EV/   V/L jiL   yx+  ``\       y    W7|y j|    nYP
~~___qx- ... waiQ3\L ` __  ____yyjy    |    $##+k  W#|P`| 1   y/_V/AN4|L      WvG1      |          | ```__         jj$__.4wj|  4|nYN41L  J|Lz;Cl.x|N`___y/A  J$|W NY``    _|  x  44k        jx    `|_
_ 4--H1kWair~~~+HR$L_  \..  ywvM/Q| s.____    ``\   j|        / W4|Wd4|L    ~~~~`|         ______.       ______     J1hur4NqiL _|H|Vd$|  d$y_@h++AYK  _y/C  q|$1 __       o- _A uxX  jx   |y/$.__.___.
-__/CUJ+Wd$L__```3\xkkwz;uyg/0X ujywmKL....___      j|      _j| dfLLJ4$L     ______       ____________________     q_Z|J| WN$k  |Nj|N4|L y4iK.____jk wy/CL wHrPKL...  j  :N` 44/    WJ$kwwsMwvwuxwuwmm
$kvw /`$V`9ky.A  W71U+WF`5|U_____4___$gm+kwyg_._ ;  J|      WJ| dA$Vw4$k_____LLL.sL.      _ygipwwwwww....____.p    $ee-Z$.LJJ|L JYd|N4|LwV/Ah;L....K.2Z$hV__JlLLWzm;  4P   \. ~   __~~yYHy+~~`\V3$M/R$
$MKKK$Ww|KIQ/K__XC$2  jGW2|K4KW4l4$.W4KQ1NNMhjyp 1W/j|      W4| _`2|Nj$kkwgeeeez__sxL    jyammeccczzzzzpmmwwmwkw   7$$l1H++W41kW+wM|W4$kWA4W/|Wgmmrn+_j| X\.24r__$$|L `C`  qx       ______  ..WxPFK|  
$KCLxKKD1NyVKLJxwjrK__y/XN|PPhWzznjVM`Nj| _|N41L | ______j  W4\y..ZZLj$kWX46FFGmmmDAVk   4ddfKFFFwwmmmmR4NN#PPF      jZ|`T__d$$1  M1V24|L`5zwwxZE2L_$24L__yX#$$kW|J1L   yxWd$k-   uwux W4e.uj;J4T  |y
ZLWYKFWV NI$ Wj|N7Tkwv4; dfK  _jILJ1K NJL qqy/|L  __yx.._|   `lzzrH$Vd|K 3fK`@@PP9FR\L  WJ$RTkcC`7TPPP|5zff```      _$$___p4$P||_  Ni_4|k j__jfFH4-Ww#j\w./QjP+hq;/_    7A y+  y   |tt  NfFW4$k    |$
$gV/L N$LH+F U$VW|  jj$L.2l___jymm/A_gg|_ jjyCC.   V/A\ku|L  J/4$|W4$j|L ``  W4T77F``   d4T$$    W`Tw44-           __4$LWJWJZ|j|h;_d\m4|L IL.2$7271K`N2lhYKjZZ__4\Lu.L  `  `  JZ___/++-  `\W4ZNJL  _jy
$EEk  j+WUIL__j|N$L_.J/hr_yx.LJ/CELWwaC$L W31hx:L_Wj|P`\MiL y/`N$|_$$4|L  _  ~~ff`  7k  Jf$9/ ``~~~~~~f``         _y_4$PH|L  4Jwy|K ` 4|k m+kn__________y _______$__+k    x__ ywww4/```_   3$FW++  37/
$EK LL.`WXwkww/k +kyw_2J$D/A\W/A_-- f5jvm+W`$V`\V.uJ|  W3$hV/ __jyww74|L           Jf   |`T7$                      4$7X1U W__j|NY|_ WW3$LW2Z$uas.L.L-4$2lLW4$..wax###_L____---  `1`_  _.  j7`C``1 Wg/`
PF _gz;L.ZE3z2:L____Ajywm/KU7XKL./___W7IL_WdlKW@g@yj|_ d7`N|L  W71UJN4$L       ;  jj    | j           ;          __|j|_jY___44 N||__pWd4|_____@++~+#####A@W##+hNM4NN4wwwww.2XLlL   .. J:L.2L  w    $$_
FF jywmmyvwwyjwmmwv W4fKTC W/O1H+Kuaxwfqzppd$;WXGQZAlL____W|kwWgf$___3$kL    .   j|$    | $i_.    `  `      _     4|J1Wy|_W.A\ 4||N4yWM4|L_.__ZZ__________________ ~~~~~Y#~   ~____ysg____y+- Aj____j.
| WVTN$$$K_ TQPRQ|K_WJf_____ VTT1WWf1N$HmWUA#|N`VX\VAkyu.W41L |_yvKuWd$$k   ~~   j|y   _____jyp  x.         __    44Z|JNCLg;___y||NJ|__N1kwmpd4bw---  y.w..---....___    C.___73\../_jy4..Z____jiL..gw
;  /__jjZL..A4/w4lL_-/$__w-.__yg|  ` J|PTjYF5$__``_ `@@H;WJ$h$KM2| j|N4$L        Xl.________jiL  ~+         4|  J  4$yccqy4-__\4|k:q|L_UA\W4FF###1K|_ygtN#YMNtgnmnwuyw___ywywvwqj+KKW2Nthbp-uawwykWX4C
|k_|_42JAwycy2 WJfKW.KqyWUAhvq|Q|   qj|_ 7$WW4L___.. d$F pqjy|jY$L_ATU3$|L       ~A\u..aammwm1k  ``        W44wwq__47T5WW/N|WV4f;pTN1NNV`\VwTW2ZD/N\wvwkZEZLV$$7TR1MKNy.______ W7CLWz;N$GiLWW4#U$KPNtg
k_jlWjfKNMAhYK _JT j;Ljib/`7|N1k;___j7lk___gz$h-tgp;w~/NTFRlCL./jYKN1Mf4|L       ```~~+MMPPPP1L ___.    4          J _J|N1U/N|/A\V|N||N|Wj|P+ ~+H_W4M+HH+Hvwy++K|2Z$LVfppmuameWdAkwn+PH|NfF _`$4|___$.
LWv/K4TLW7$M1kwvKh.J|uziy;W41M4#1L  W/kh; eg+y``ymElLZ__g.W4yMKW71Ph_j|N$LL  X ______`7_________.pwk       _   ____ __JKwW4 ____j|LJ4|N|WJ|L  3Tk_ `$FSTP7XU7C1WywymWd6@P+H##HV/`NWNIC____C..2/#1hyje;
kWf1Wy|WjfKR1WJ/hj~__W@M/L /#Vff|____`_gc  SI____F5wywuaeK 31R\|||___j;M4$L_   wax---.....wwwwa--PFF    ______  _|  _44|WfPW4: W4|__OAN|W4|k  #thjyw4.N1N__/_yWHfN7PPPRTC`_T```L   ___u4xwvrny_M|KZQZA
Kj| Wf$WJAK______J`NV#P8IN2c__..LLwa.uzzi__@4ykx-KZlN$N## Wj;N4\y  qx/lLJ$LL__  7`#f~~~~~~~ffffT5L_       |_|   41____j|zK___~_VJ$|N/WN|WJ$kK  \Uz:wzr__Nx-- J$`| 4.   | _______gs..$kWffKZCDZANvkW4CP
___  jwmrF`\.L eeq_______gj;.g++~szz+vwmik-##2N55~gjyfK`| qJ|__\lL_df$FW/A\kL___     wwwwww7T         ______|    ___m4q|__..____gJ|M|__|W/`\yW _gg_W/4kWVf$__q;___g; _L.______aGwwrp~rq$pwq~~fWM|K`4|_
k4|W W7A1L qiL@9F9w--w44FwxmKW$Z_zFEZ__5$KOhtrFRKWMTlLLui W4$   4+W2$$W7ZN4\kkL___   P######| YV ~   _____4y| ____44MWU|uYXtNwW4hf$4AWW|Kw.2;L V44$NA##n~~wywwywvwuiwqmpywswwmmMKMTKJwM|N``T ___|  d$W
|hiyWN.Z$x_H|____2Z|5f#f_j|ELgsg__E5sy.g|___j;______~-___  j|   7$j;#1hYKWZ7N$kmLL__  `````    _________|4#A\L_._ydtrWM|Wj|+W|q|Nf4Z1VN$rj~j|L ~f#tKV`W``_y/KUIPN$H+yd@D1N+H@@___4L.__2lL__. uxg.wwW+W
|N$KLywWymWUlKKCLpy  |  waxHmw###|-W7kqpi__.2iLw.LL.ZILZ.. J$ _. w7Z___|  jyM7PNhmLL__     _________-wpvk_____uwm4FF__$;K4.__|N|___g_  4|J_j|k-  71_______/`W4|k TN$|P~KC``Z3$_gz.kruwxmkwzz_J$q;K _lu
kU|AW/WU|NykrH#jyM1LU1L WdfPTPR1NYKW_y$PkkphH+H@@+++++H+++WH\|_yPWAL.-___ 2lJ$LZ7N$kL_________.wyvwyA_____auwwMWHfKN1W4rkntwy/N\Lw$4L.N$$Kw4YK _____iL....  _J|L____|______~y+yg-| _W441N@+Aeee3iL__+W
LN$Fj|WJ|N/K|LJ71KL_ Au.____``kwdmcuadRlNzWW2ZELZZZZZIZ`TT `J\VAK__jyKNvkWww4cLp/PA|hkwywwgg____2|___..wyw+HR1K___lJ1MT$|UZNJ|__|N|gj;W7|_NJ|L____wyrk~njc_uiuiu.uwamnwyxKC.ZT$CCLL..#zcL`___~FP+hW4T_
kP|KN1W`|K uayW/A4vx/W3;h----wM4TF+H~PP+~+--++F-+++-++  __  d\Y _yWM$.#tLLV7$KWMKN4TNNNMMANNMNwmmwuwwmmdfNTPN|wwww+PF   _ywy|  4|NmYn|W4$WN4$LWJDWMIDN4N4N-H++yymWdfANV/|NtcpxwaXwwmr___  s..7`_|  q.W
K__ d\._  Wd41L` jf5_WZE@ZZZ___________`Z`WZZTF7TTTTTTL_$k~  J1 JJ+HnrKFwy; `1$$PWf+NWMN|PPNfM#fNNMPNP1P1N|_d1N##P`_    aYUJKV_jKUJ|U|Nj|Md##FF++~~~;n###__K`777fNj|A4KC.W4FR;zZ|LN$lLL22@@ss;L4xcwyxW
k4vwyyXn.WWd$$k__j$wwvwF-----wwm-wywwxwg~~~~~q;   z_5. q+F   d` q|$l|   M|K__.J/ __|`|$3lL `````T7T$V/NTTN1 d|K`1    __|MlU;hj4ZFW`$V WJ|KCZ|F`7NTW7wMwmwa.uus.KWU$MVP~~~nMNNmwmwkw@++hynE57A\Wg;~W/`5
_j;LWJDM+__A4lLLWd$MRKUTRNVNV@PR1#f###T``TF`Fwvw_yyw-+_jIL.___ _jywj|_..|ID|wyr______JZd$L        7P+ \11NmWd1        Jq|$$__JAjC__j| W44U_jiL_;##WfP  ~~~~~~++~~yARKKT7`7 #fFF21KW``CUTN1MZOD+wyy7  y
 4xee+N$CWVPj$h+#+kF5zztzz; ____ g| ______   3$LuzLF`5 qip __y Wj|N4|wyn|pY|UZ$Luq4|W4NN4|L        `` J-PH  s:K      W4N|PAkkcU$Vkqq|WW hY44$k/______________`__2T   ~j_.  _________.zz;J`$5|``Ul$  j/
W2$EEI2Zs#:W4TZTN`555FA-mwnywa.csq. qya.L..___j_______ ____jyr__j|LJ|U1U|L_ J|j;Wdj;N4NNM$LL _        ``   Tf`     # ` N|C|7fhWd#fWj|   VlU$$$L_wyewxcpwawu__._________y--  4W44---_ywwmr _j$ wymcL_Jw
m$FFWW/FF~+ ~~~_____ZCZZC55/Wd+hwjiudth+hmxL._4_ ._j....4..24\WWJ1WyWM|M|L.w|lJwMWH|NwMMPR\kuw      #-H1       J       7A\xL. 44O N4|   j|HA#4hYH4#MA#W+++H4vrKC..wuamdZCL. z5ttVXK$DP#fF wv/KW71FwW/H
N$F`W T```TkwTW4y/kw4--uyx/  `|KU7+Hd|P`N7AhywcLzd5zamwwqtmy`| dfF X  qYkhtu++HAN$N$kPFFF``WVA   _  `  3       n_     W|7T$kqy__y W4|L _$|P 2|N1U|KK#ZCZZI23XCLzidWMQDhkumrn--   _yrXCI.  Vf| yq$V/P`U
A+____L.LW2lKL_jiL___$NV/KL__qiy//`N7IL   N9fFhykke@9$KWVTN\K.W7lLw__wdfkU1NTP_N$PPP```    \|   .J$   .     __ \:   .  1  _4Qywq|  j|  j41kW3|N`Mi|  wwwmwmZ$wW4APWAN4R$HRKF`@__jy/`_y/k_ |j|dfN4rK  Y
_l5xgqzg~~~+___gm-u.p/#fC__z;Hgg__  j|kW/ W4$WWTC5$E7$1W|__|+wy|A|kw4VJ1U9$NwwWPPKC      _  \y  ~++~+       s:  ~  z: ____;nj|NJ1LWj;K Jf$|W3|L 7AKL_Z2@9P___ ``F`T77FFF``E_ S.u3+AhW/Ck _|J|N$MfF__uJ
_y4+AHxkZ____4WYZ1NXKFk|ywwiWN4Gmk_WJ/N   dj$W/A\V|NMy|N  ./NWM|N1L jY`$V|NM#Pf``      wee. 4.. `7T`         ~  |--~~ w.wyrd4$W4| W7|h|d|_| j1WyK7hxyw---`..L._.   __``___y-wg+V`C_WJ$L_wwxmmW`N|Kjy-W
NTRTP71N$---#4Q$kWUI1 _$VWH+P@/##EhV/| |W|M4$PFP`\$Z$J|W m+ww|M1H|;vm|WW4K$/F`         `Tk;  ~;       .     |   |`T`` XfQ|AW4|_5|  $|W|j|P|W___|$WWAKCC| ggmmwu;L___   aw4/KW4$ZL..W`4V4WMARE  q|WJ/K7
K|  WJ  T3M|NWMfFk+F  q|K___$Z _|  `__ /qlMNTF|W 4Nmq|LW|7`_j|7|N|k_d4VPA4yK            `4+         .e-     |  H      `\41P N$wy;W y|__J/P\V___y/AJMPhmiL. @MNMlL -y-LL999$k  # WXAMW4fPV`_____j;W/CWJ
L ______JJR|WX4$|L`` W41kwwaxkWw.L W4|MWM+FH\y.W  7$MkkW| __y|_|N|LyMrKCUJ/L             ``      y/ ~+`    XJ/    \     J\y. J$$1W |hYW4|__4uJN/L_Zl/NN$kp_____@K__ZLEE..2_L.LL_22LzsJ___  4.-W7/_|V/A
L N4ayw-eJD|  `$|w__ wvrNV23$L ~+kWdd$M_|` U2rhV NJ2f5 W___J4N$WH|M/KC5xg/F                .  /  4C         f     ++-  __Jz;uJM/L  |M||$$Vd$V/#1  44  /A\VL_|__A\WyA-yyFnwye+~wymmw~~cL.._gatmW/C.____
L Xm4|P_jjM|  _||N\..___  w47K `T  W#A\u.waedTP  W|` ___jyx4NNPKN2NCLWYKj|K        .      ~      `\.           _   `  \uvd4$WWf$1W |_qiww$wW/____________$ywygc__y/C@VTCP XT`77A1KKR$kx+A4W4PPP~9X44--
k  `7\__J1M| _jy_Nj\L__..  7$\WW4LW/N`WV|__TP|   J\___yWWffP|K$NN/FAWPA\x;h       +--     `  .a  .J;           a:     WtfOA|_jT tLWlmM1K@2LsLL.wwwwwywww444M$mmWCZ_k-s:L..LL___`______````5 `````J/f#N
K___44wWdfKLLW4l$Wd$kWajc_____ -++____/$$W.4$L  __j_WdfMNPN$1WjmK$ /KKDM4FF  _    ``        g~~  ~+            9+     J$yK`_yy__$WW@BR$V#-F++~~zff5tz22222$5$@NhhmwC_g~g~+----__j. __..  _.____.g_____
L--wV/1Nf#hhvWdmmWW`1W74\k--..__`Tkwxe 2d9fhfK __.ga+HfkZL z|U41Nk @@XY/``    .          /  47  T7             ``_.  __3:hwaiZ$W/##FE_  5$7TTFFF____~~~~~~~____T71Nmmu_WTTN7Rkkggz__g++__aip__uiLL.  `
W`#P~  7___7+HTR7__|  W4#Mfhmmw._____|  A-CD/__yymmPPN17-- jjm#KNFF `55;     z;   .         `                   wv  _ywmmUx/A+-__L_5www y~______...ZT7TTT77AvwwzZ 7RNNVWD|_/55MkWyw4/Z1WwmAkM4MAk+etc_
L_KCC____4 /``T_\sJ/hWWNfRTN`N$kn_--s.L.``F __yV/R|LLJ/K`CLJ4ZR___   W++      E_               /       | u       `  V/d$FH`_S3$wwy--~~_____.-v_gggggtg_______|HjxL_2_94hKC. W/|N9XW44kzcE_____CC`TR\Lu
k4kwwx/kc.z ___zg~+kW/fZ$5wWvWZ$WWM#mny;   __y/f$Iqyk    qgd$$kkK_._  `       `sv/ _    .     `                `   W4$~j_S$wvP~~_``___.awwwmdsUN$$7F4wyvwmwu4w.7|\yw-CZ|A\YC__ W2lUf~j+Fw--.____  __~V
P|K PR\Lqgqiuwv/CZ___2 wm/RMfKGWMtWM$DP+____J/$k ~j|KL. j4fNfFhfhjiL___        7|  x   y     \.       _.___         j_`$vg+______ aawwmmN_A+F~~~ff_|_22LL||gfh;nTMXCD\K4.J$hyL hmmwTZZI225h~mxC..___`4
L.L___jpwGMvW#fF9mw4--_______@@@______`___yy+Aj|__21k+;_j7FH|$WAN7AbxL._____   _|.    N/          ..  --  .    ___  ` _jfC5__ywwywW4PPP$;KZIZZIZZ$wwwmjy-wymw_|Nj;h\V4D|XN4QbL___2D| d+wwZZZD5~~wxcg_g
h+kwww//@99KC`|57#c~5`\..4..____ST`  __ywWM/F 4|hVmP `_Wy/KUlkK ___2zhhwv...____y__               z   ``      ______s   _yaaMMANVP_$$5wmmnmmmhrn~+H1NNMNTP1kh4:NJ;H+~j|__ 9fMKkrn ..W4OT#$k__ 7`Dh\cc_
7$\k__5$_2/F  y/ \____gttrntg|. /pV __y/##P| WJ$MfPL _wV/AWWfkh WjyyFC2Dth~~---u4LL____________          ____ wxwavP____J$NPKCC2$_wyrW4M1MPR$MTF`TN|N\VJWM$|W/AWj|_ W7Z|w.Z`$VU$L Xt.   ___4Vg_  `4\hx
_$7hkx/A4ZC  gc__ 4mLWW4|__ avWKNV/ wW4fPR\ywWd$MZLLW447CN/A1T _yWfF_yW/TF``DMX#+mmwww-uu.....L.__________uixw/4_2;LLww--+K$L___g4U/PNf/$F__| |L |  |Jx:L j|K  JA1v W+g4P+KLJgjyKL`$___  .__tpx/   $7t
utcL2___2$k__$\k.2~A+##44WWdJKL     dd$K _J| `jy;h_y wJ| W47/  y/N|_y/KD._qyWKCTZT21N@Nhh+~mmwywww-----www@@___u$v@+~~f$ZZuJaKNkdW/|_V/h7 Wyr |L_|P 4dA$Fwj|L__ M|| NIU$Z1kk;$5$kkWu\L..gjy_TPA\  dJf$
M4kwx-.._`___4Ph~~`7IL`f~~~~`@@@@--_44TFWWJ1WW4TTNj|__j| wWXC WtKN|y/+P___qrF\g+pyw....TTTZZZDNWNQNN#X#NVVPK_.wW+KK55wwmmmydfPNfN7K__/    WJhW1Hd|k_______2$k.___4|.__W|g;  ++eAKC|Wmm~~yAXM$LL______j
N7U7#5XiL  2##C____.~L   `_____`___3TZ$ WJr Vwdf W41W42ZWY`\yy/`Wjy/AKLqyzd1k N|y|ywrrnyjrwjy/#.H|$.K$V/AK$wv/KKGkWWdfPRCDN|K  _jTNjY  _j;//N |N_|Lww4444Wyrh;N|LuJk _jjy|K__7$7|\..NTC71Mf55bn4---4_j
k K447Q\k_wmmgwumvurEEEi.___j.K  WW4TF___|F _|d$LWJ|N$mkH+ 2l: __J/PR\uu/FRlL_JnYu/OTKNYJ_j7||N+HlzpvWc5$k___C_ V4N$NT$$mw41M|K./|WJ| _WyrFCNlwwm+P~~~551#fFj|N+mH+L .dJN|kwyWAN.NiL_  /q|_ 3|RQtWYA\M
   W4|N$kVPA-_@@RtU5$FFjmpxWMAH9 WW$$DA\41__ygg___jyd4$K` WafK WWffK $WMTCNywy/M|#|y/jy+jy/qyK/|NWPP|$W/;55wwxe~+___y|myfPj|__yj;_y/ _Wd/C__ym+~~T5`  ____`W`1P T``_yg~H4Y A4|wj;HA\L   N1K R|_j|W;H3f
_____$MANYKN$kVFAxeL3$VAWR1N|$_____jfKNJ+KNyg|C$.W_TPj|k  _7FhY_J$|LW/Z`__W/KKQY/7_YCV/C.X4U/kpx/C55x/jGwW/NU|KC|__2lL$7A q.A\Y`|W/K_W4/A\y./Z`` ____$$$WwAL $  .__JJ$P_7\L2J|_J|W`$L____`__j\Vd|N|L`T
:w--w4Z$M|kWtN$VU/F--+KQ1D1K ___..2TZhxZ___$MwMAtkW/N4|h  W71NwymmrW_|__wy//k_y/k|M|W||y/nyM6V/f` W/AVW/P1$uwrhmuypMwyr|__j;W/|V|YKuV4MKLJ#KGwwWK4G-Wn+#KN_$y __jyyW/A\___~+M$WH1kW4$kw.__..___N|HiL__
;HfKN$N|Q1F $PA+K``@7PR44K4NW44vmny4__jA-Wd$PPXP|Vm~Wj|N|Wd|hW4T$PKW|w|gM/`__y/A4WN|N|k4|Wj$kK`_ WA$k_____|Mf1__NfPKy7A|W _|KwlNxCuVwy/hWd#1k/K`yWdfC2I2 __jlL$JwM4PLW4\_W71N4|N|_WMfhhwwMmwW4vH|P1F--
F   W4Q$PFFWTC7T      `2f`\Y  jf|___$-CClNM4r  4|IL _j|N Wy1WWJN||WV|N|E$;k WYANJ+/WM|Wywux/F _y.__|.wwwmw/K___ M1C 7CU|N y/kH+P$$W4O/KUJ$P|\|W_|Z__ y+___44yW++PR$| _V4\V  JA1NwV/NTUZ|WMfFU#KQ|NZTW4
N____jy/F`  `_ `  |~ _____     |_.; /thy~ d$lLdJ$kcLWJ1N WZ1W2|Ny;Wj|Hj$PFNWM|y/`lLL/CW/P/`5W v+K_.jyd+M1P|__|p   y/AW/ALy/CV/ANW4f#7|hydA_.p; j|pw-W4I$wWdA1KTC  j|  4M4iLK|P\VLJ|__yj|  ___` N|kmkWj
_lLLuJ/FL   w..   Z__\. G-.  _jygmmc _d$C _j;_~dfFF+W/|N_J$FWj|UJKWJ1N4$FF _|DY|  +y|N4|K`y////`kWdJPMTD/ _Wj|L___JC_J_wy/wyrA||PN|K |W/Rqy/P  J4K_|_ammH|KN1Kwmm J1L j|H$L \V`+HmmWJ74|L 3YK. 31N$LWx
mm++#/`  y  df\   \ywzg~d| __yym$$AELW4PL d$$WT7`TC|_$| +HILWj|p/kWJ1UZ$FWWJ$V`VWd$$WMPF W/FK`wd49PK  ____ J11K_wY/hVANV/CW||Nj|  +uyrKC_jfFL_ ``_wyW41KN|kH$|L|$ _|h_J|N4lL`\V`TR4\vwd\LW/|h\ ``N++W4
jTT_________________________uJf$PE_A\VZ$ywW+|P+___wywj|K 7\|WjfP|  |hj$Z Wj/A|W/A-q|N/K__J| _W4$MKC|  K_|jrH||_|V/NW|$W/hWW|kWj;K``V/___Wd1L_i. _|Mf|$$ N|KNM|N|___j|AN|N41k_~+_____|__A\L____________
_qy_u.wwwaywwwwwww___y.____WdfFKCS.22F_y/T7T1LLu.WN|NJ1L._J|WJ$|LWy|W3$$LWZ|N|__|NN.K|_y./_WW4Mf|LpYK J4MMTK41NJK| J$__|W4yfKW7|hyx/CL.xwj|yWj+Wdx4$l|N|N|_JNNM|k_wJ/ 4|Ld$h.Z| w___|W_7$LLw.u.wwu.www
d4fkdtNkdf#NMX#fNXN4NY:WyxkWd$F _j$KC WiL  ~;~~d~+N$Nf$kww4|K4y|__|| jj$kWuwy|uaiuJfK_yfrNyWU|55yW/|__dJ|N| j|yfLL_y| _|wyZiL $LV/N1kW/AKNlV/D$WJ|$|A$PA 4x/ __|k_g|__dtwj|h+uxcpavm4NWfQ$kuwVfRtHfNWd
W4fK4AHfk@@~tCL;__zz5fhyzKIL2lLu.JZQ|LH$ELL2ZZZ5$I2TF~_| N4|_N4CL_|L_$$TK_UJK|Wj+k/`_y/K___$kewv/K`L.qy;L_| J$7AVKq|L N|P/AjyJ|W/|_ NV|___j$kMAHAV4TR|___ff\__y:nw4$LWd||J|N|N|k_j+Fk|j$MTFWPTRU|P1F_j
_ZIL``P\5j- $+-- ___Zl9XANxkH__y+R1H+F-@A+--+___| __  j|_ j$LJfhWy:hJZA|Nwy/hYK$ZT _J4$kXu./J1P___grnWTFWV|_drK|  NlLW91K4$Drn__$-k _j_u.wdfNfKN2Z41Nwwy __|wV/AjyH+K__jwy|N|MK4N4TW41W41hKCK1MW$KKVW4
wqyg____WdlWKC`__2$S--df$NIL _JZ1_|RlL_`7T_`___Zl.L.._j$kWjmmnwwW7|Wj|D Wjf  |qmr _jyAKK@jf1____yrH|_U1LWfhWX|uY  J$kWJ||NyK|U|V/|___4wgrKj$_;pj$$___|N|NWVN|KCLJ/NI$LWJNYKV|K`__j|Lg|N|$VD|________ #
_j|F--__gg;F___ywwWKCCk gjA__gg+_JxMhx-A4.W..axqj__j_u2|K dT1L_WN|_Wj|___|___JMfK_WJ/__ W7ZC._px4|N|mN|__+N| |M| W44|NTN|U1FujyKK  yr4$Z$LwwN$VWArh u.J|__|N|w W4;W+rhywj1N4|_ _4ykg;_ 4H;N|N..44...__
_4lK |NqWKZ__yv/K___aYK_.JFw4K4|W/AL__________jjmwUIkWj$________J1_WN|___|uy______g/__._____w______||_________|_____|________4|______________________|N$__________W______|__q|______|___j|__ggygtrj;wy
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

