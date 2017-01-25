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
