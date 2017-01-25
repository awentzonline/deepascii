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
Predicting...
                         _ydfP___aa#NPPRKWZT$NT$NPTTPPW$RCWMTPRVPT5mKD#jaMRT`` _.wRN$TTTTTTTZZNNF$F$L___j_                   
                    _y/ _d$FagW#NPPj_____ZDRDRRRP\7F`q7RTq$PTuqFuWPLV_y/CDF_~_a#T$aKKVP__ap#PT$m#PNf55mw#kg___               
                   _y/ _4PLapg__.aappVPHMDkRNkP``3k_q7RP`W$W aPNP$DK_dRNPFyhWK_pw#F____a#P__z_I___apAPPTNNNNhkL__            
                  _V`_j4A$MPP+__IIZ$NDhm.TRRPFW8WXC\QFWa+d$WWT $HZLWMRMF5WGPhW4PF_a/udPF_udRP__aAMPC_appppLZZ7Mmp_           
                 _/ _yd$pPF5aam##RRRRTTTl5FF\W3L~`\VRC.88d$LW$Wd9PNZFPT$MN$KWMBFWdFWdPFuWZD/__Z$#F_JN$NNNNNNHNNMNL_          
                 4 _d4$PCLp#T`Sa-___.2g#F5Bb8F#\uc```7bc._7FW8`3TW7TF qfRd$W7P`Ld9FWTFWTRMRbdM$PFWp1N$EZNNNNELNNM$k_         
               _/ _/$$$gdP__aw4$W#PR$PRFFPFR88ka8#h+W88GQmmL.`3``3TP\W3$WTR$F _d$PF7PWdP`TW$R9RFWdLWdPN$pNNNILLNN$Mk_        
               J _/AdPNPCkd#RDPRF_aMRkPF~ys@8K``5su.3a389RGZ2~~~~9P~8.WR$g3TFWd8TRs```TRWa7TF` TPPPW75WfN$NNNNhpZNM$gL       
                _|RN$kCpMP_awPF5a#F5DPF_we-@FW.P38P`3``..```\wmmmwa.``_.IP\3PW88$@~-d8P8`58Q. 7TP~Rd9R  7R$ENN$L__9$D$L      
               _d$W4$u#FF_dT5k `_ g$$kWPF\s.....`` as.s.`.`    ```T`@+W``\.P~_`TRk__`3L`\ac`` aZh888``_``7T$NNPPFg_jEN$L_    
               jTDfj#F_pNMFW__aw/5dPFSEWmc```v~j. s@`\```` .`  _ a  ` -` ``~mmm``3#hK``+`T$ .`T``.38~39am  T$$ggg_\UAVA$k  x 
              W|K|WZ$pP__Jqam#FLp#F_gRFF``sc..aeL.8L ... \.`umwm.           ```__``` _ ~-`  `````3...`\87P W4$ZNNmWZ7RU$$L   
              jfN$_jMFWdRLd$DBkMRkW@RFF.`.`L..`I.$.````   ` ``  .    +     `         ~ . +~  `` ```38.`3888``T$pgZPHLW$Z7$L  
             W4md$WRCW4FPH$ZT5pPF_DF`8W8@F_j8 .3BF`L `    v v/ `                       `   .. ....``~~.`38~8 W$ZNRLW4kP$qZk  
             N$Pd$WLWfR$ggPK_4F_g#Lar`WGsoag`W/F_ -_j/    ` _               ~           v  `  + .  ``.~33888  T$EPh__$LLN$L  
             jT_J$LjWAgN#FLW$FLNRLkFgsLsL.`be``W+ ~++  v-   `             |      +   .  `       `._ `_`3.3.`3 W$$LWAkZTNhA\L 
             | qmdK4Ld$$FWZMP|P_pPF@g@@F`bc@P`_.  ..  ..  ~-            _ `          `  .  .3-  3As-~~~``oa.`  f$Rk`7$mZEW4\L
            WlL_$pL_jZECaZF_amu#F5pa#F`scC@\_ `F  j/ _``    ~           ++ +     +    ._` j_     _` o-am.``..q d$KC_4Z$N$hg$k
            W$LW$LAW$PjZP_W#$PF`_$KFLsL.@RLaxkc. Wf  ~ .. a. .`_               _     ``~+Wd+ .   q. ..`.3s``~3 d$L7qgJ$d$NN$k
            d$L j$p4RWP5a#C.`__dRRF@#RW/`.QZ`_38L      `` ```  +              vA         +   .  _3`.`\...3-_``3W`_ 4OhLN$LQ$ 
            J$E W$LTNZLdPhdFWdPLpFL8ks8FW.Q3FWx         _.. $ w- -    . .  ..... ` -  ___y  `` .`` .`.Z/`.um~\.Wq__W4N$LA$4K 
            |4$LWA$PHNHRLdRkdP5#FWK5#F`.`.`$y/` `     m /`      a-    ` ` ````P`~     y~+\.....____` `$._-``_.~ \qg_ZZZ$W$$F 
            d4ZNLWT___ammFC_SpKPFSWR$mcL_`.38@~ `y  ` ``_.__  . `   ~~   o     y         a/ ``~+~W4kwa/`~-`~Wfb Wd$LpA$Pj$Kk 
             TmkwK_+hg_ILaKWPF_5aBBBFFRbLWam/_~  /      W``` ``V~++-w..    _             `..mm    `_ ``..  `_.. q_TqLWjqmMK  
              $$_aaL_q#KjFW`_gpRBRBF`.@PF-`$@~+v .wx         v       ```   ~    ~am e .  .`` .. .`2~_.ae`` ~W.3 W$.7$hq$RT   
         _.ae-3lqZ__gZ$WRL_ga#RBPF`L`8F- g.$E`. .`   _y                             `.       `````~`3P`` ao -|qoW|$W4qjPN/   
         ylL_```X$mn##FP_W#P$kKF`WsEs.oo.j8F``` .   _`je _____                _      P~~ - -      . _ .ac` ..q/`W$gLWaBk/    
         fRRk_  ``5VmN$wmpPKJFFF~~388L`.aaF y____--x~y/_yr@\ss--.______                         .`_ 3 ``\__..3. W4$LW7`      
        |1`T9kL \ /T$_$W7F_aRkKL`o8@8F.`3`L_ggaA@@x`amwW6wwMQ$LL_gpaggg-___               _____ __yx_____g@ `3. W4$$KK       
        |1 j7R\L@~ ~ff__gamBRBF@F@Fo8k`WZ_.dmRGw#K`W__________99#RPPNMRkMk`.          ____yx_gggg___ggssgggg.`3 W$$$C        
        |_ j$W`\L  \|aadRBP5RF .s-.o8q.3aW8P557`___awm########mk`#~W8IL__W@L`kamk.g_  j+~WAGWd6BMm#mBbBP@8@8bL. W$$R\x.      
        4$ 3RL d$L `TT57T75KyL@L.._`-3bW8F`qs__ua#P`__________`\\___`TfRbg._@@``.A6~  |_.ggL_`_9PPPPPRBb#mP@96b W$BK@8k      
         \yF__ `f$L `fF\4uiWRk````ak d$./_-daWWT`__aawm#@####ww._9bc__gg2RMk~~   .  __i##@@aawmmmmw.L___``\wg3$ W$BN/F       
         |$kqg wvqL._`3q$dNKKWgL@s`` aT`~+.....aa#P`\4Famwrd$ `\bL_9MMMRmK3L       _adBBaa#F`________9huL__y98F d$N/`        
         |F 3$wwWMRkW/ dN$KT jF@L`spa.`   `39#P\$C   d$CZ_a4P  ``9Aq./`_j;`$k      dBRF~_`wwqy#@N|N#hwL29kkom8sWd$/          
        W| _g__3F`37F\m~WfF\W`Ssk@P_3\    `f.. `3$k-__`~#PF` -w++su7PL-dfF3$      WTCawe##F WfGvwmW$L`T\mZW8R8FW4$/          
         \yW6mg_  T$ |F3``58Log8EE-aE`. _   3$w~``TM@mwwx aaGG-wm``GxK3MF```      W$F~wmmxc `\KZZ_2PF ud7FWGW8.W$$\          
         `|_ A$k  q$WjL`.2``5Lgg@\@``.` `    3.~sv```___`_````_I$a@#8WP``qf~xL_    3\ ```Z`` ``TPP``___23mL.`. q$R\          
          f$L_3mk.j$ fP@ZL.g~888bGc__`@x`    `am`~swwmmmawawmmW#BB@#7`` .3: ``~   q$P\WA8Rb2``+wmwmwmmd8FZF``~ d$W$L         
          |7\WZ `\vgL`$@8L`s.o38F@@@6kE_   _  `3+~j ``TT`TTTTT`~~``     ``.3s.    d$L`\L``3Rmag_____amR$@Pk `.WfF@4L         
          \|`P\k `TN$W~ss@-qs.qsLpoa8F@@k- 4   ` w4+  ``   3P~       ``o.`38P`    `$EW/`\k_`TTRRMM##RF~f\. ..`qILj/          
           1L_`$`  ``|gFF`.@3PW85Rj@8F@EL..` /    `   7`           ._.._`~_$L@+  |`3$g`  `8._. `s.`\s#ae/` ..gd$w4/          
           \$eW3k@~wWfEwaoE@8baoGggsg@8hC@WE`` .      `            `X|g@sud#F_   +wm8$W   ` ``\``C./Rs/`   |igdRa/           
            A$_`  ./ q$PE`G888@@@Ry8@bs`2EL``  ``  v             _j.w36kE.``WmL  _``$$K `\o  am  2``_`     |lqp@/`           
             `\q_____j$EFos.X`..~W8@s..W6hsF```   -   v       .-gg3RWP``8$@\. aL`+~vd$\L  `. `. 3~ -yx  ~-y3W#R/             
              `3\wwwweAF@@@FWo88L`amgL..`a$F-`_      -     _ amWQyF``` _`$ @/  j;  .3$8\   `  `   ..o`  _dQB8gj/             
                ````T$L@s-~\..`3bs``qL`3b@3L`@#m-  i __   ad@#  q$____________ _  ___j8$WkL   v   `.`~~ydB8B3Q4k             
                    `I$F@@s@8FqsP`.g3F.`8@P\c` ``\ ` ~~  _@#F   `\qL_ga..___ ` x y g_g_yF`sy      `....q8P89@3/              
                    WT$bs#c@@oqE oqgL@r.`\-@+k`  `  `   3#F   ~  `7P##PPPNmmL._____aapmK  jE x      _..d$qaaa/               
                     |$8G.Lss.3$W3QZEL``_aoo- .__   __am/`___     __     `T7Rkgwa##9PPF`  `\``.  j ~~.|:3gj/`                
                     |$QB8L@@s@8WCq8RLou/C. \..  __g@#F__.WA\L .aw#F`aw- ``IPd$NPR#~F k `..Ay__  v- - y3qj/                  
                     |$8E8EL@@8q.`Q$E``8FyL_.2`__aPjsKua#Ay_`~j.___x_`_awmP`.`$C`j_  aF-u$F `yg  `   `3~q3F                  
                     |$88Bgb@E@@FWd$6k@Ga6@W/`umP\aeLL`T__g~w+y+W##`W#/``9+KCWF``fyg-__.2P\`Wjy   aq./8qj/                   
                     |$83Gaeggpqswq8L@oGGq.. /8  yP\L.xq_____.sus....as.._________ymc@Q@P~~ssq$pL.`39~qa7F                   
                     j$~3dB$gBL@$L3ak-.q.3$L.s. j$.____uaam@@P_____````Q$kxggawmmmi.g__\vcg__W#FF`~~~qg4F   `                
                  ___.A.88366bg@9kW3$L_P\d$L@/` ||P####F`TRmm@@#mwmwmauLZ___________@~q___8W#$F   _._j3/   `                 
               ___ad#KL.8a8Q$qgLLssd$Lg_`T$L_s  d$L__` ~..``RRmL___```TP############~wa#RkKZa$k   yyg38F                     
              _yfRRN$K ~~8`3B9#$LK8L38\c j3\ggL _3+6Mux```\._`3RRMmwcuau.a._____gygdmWT``T7`7F   _ydR8F   ` ``               
            __d$PPNZ$L _ooq8R879$Lgb@#8DWA\`Ak6W@F`sZ``qe_`3mu___`7PPP99PRR##M9RmmB#P\Q8F`_y/ ___d#Ry/      .                
           _y/$$$ppN4k .AsP\8\8dRMELj@88L 3+W`$6ue.``~_``WmG`36wae_________________.ua#F yac _ap#P_yF      ``                
          _y/ 4$$NNN4k ~W`ods`3SdG3gpg___s._g_``T`g.~-~mug..`..`TR#RW6k@Wm6kgpwamwmBPF\guwQ$w#PCSu#F __~se `                 
         _yfP d$$NNN4k @@anom9+8879$FgLgk~g__g_sgge- Av.2@9kW`3~~~~sWIBW07FWPRBPTFFF`g38Kq3F`uaWQ8F ```@$@                   
        _jfFL_W$$Z$g$k `.2L`\.ao8\qiW9RkgL@##6W@gsL__.``~+F\.`+~- ``338RL$aC2c`_`__aa88`_3$L/#`j/F``sF``8` `       `         
       _df$kP5WT$$$N$k -E38k`3GamWdRq$P9RLL_7588F8ka#CW.~y~`_x__~.P`````~5#R0##ha#~R3P~_g6ECk_a/F `W8L..`                 `  
      _d$PFLLZ W$$$g$L-L@8L`ag`T388WT$L_2#kgL_9P__gZ$W/_we_3Q@Aka/_;qs_.~j. `` `3.~~` wygjyKu3F``L`.ZSE@`  `       -      `  
    __dPREppNbLW4M##Rk`E.@sW@9F@R888WTR$L.2$W6k_~##KKLw/`7_`2\..3k__`3#kW4k .`__``..xuaqy/AW__ d8@o@@@E_ `         ``        
   _y/RLZR$BBFlWZT` $kWP@sC`~~~s_`\.d8WTR9K2RSLgg~sLW$$.__s8CW3K _@X@__. `____@@P 2$ /`d6k/_jL. -``.@8@@@`                   
  _j4$FBbWBKILgZRL _jLk@~@Rkg~`aeL388``5dR5qLZFqe___WW8\_y/_.3Aku/\-.g___axw~~C -.__..amZT Wf$L. .@@88@@~-.`.`~              
 _jfP$WZFNELIZd$d$Ld$KkL@+`3RbL``fC.3~39R9P9R$bd55#FgpggamL_AL-.___3C._y#P`\azA.____L$EZRL j$RNL__@@8@@@@@@@``@oo~- .        
_a4$RRLZNBBKNBKDU5LW4kF\L`\C``AkqZ.X...`3P\82P9RHKLWRCPbpEgigL.gggyK8kyg__._____iL2N7FDPF W4FENRkL_..@``-`````` .```Q.`` ` ` 
P$BELd$LLL$qZIBLBB$Ld$k@6L@F@g``3RLW+@#R$Wa7```TTd9hWZLP5RKDR6KdE@ggSgpwe_iuamam#RPBDP_g~_d$ENENNkL__   ````3``.`.`.3R  `    
W$RBPHRR#HFRbRBBRERlU$LyF@sL3EWGs.`vq._`I.`3owamR8C3PPRMREEpP$PPFPN9FAkuaMRMR#P5L_9RLW#F_W4$NNNENRkwq____  ..  __````    .`. 
MBR$pqgpqgLgIqpgpqWRKRmkL@@g.\.`36mc`\mmQ8L8`g`5a8@``g`57T9Rbmbumwmmmn##F5BEP`56mggF##PW W$EEEN$EFKW7Nkpg___________    .`@`
```

```
Predicting...
                                                   __.wd/APPP_____.aawMMMMMNNNNRKKCZZTT7$$TTT77$$WP7TR7TD7PFW`$V7P`1W7$MRTNPRRN7M7TCCS.W/C5DWMA__$WM#PPTT````` __$$w/PNZ$$7TNTPTTTTTTTTTZZZ$$NWWFFFFFFRZlL__I|_ jy                                         
                                           __yv/ __ygdfPRC$__LaaawamdRZZ2PPPT7TT59+hKwZDRNNLWWNB$kKF57RRPP`__9M#$FKWWJTR$$PRII2fF___am/FFWW/K_SaV#R$$TP  ..____aam##C$$9PP__$TPPP1____gpmmmwmPKTCZ$IDNaMAkkggLL_4LL_______                                 
                                         __yy// __gd4TCC5aamww##MMMPPFF+_________ZZ2PhhVPN##PPR#PFKQzPPP``_aa/PR$PR\j|PPRTCuqmFK__aW/PFLWJF__az/fC$7PK_ g+__.aW##T$_jaZKKC5V/K______apmRRRPR5$DqnmmhhWfff55mmekuamkug_______                               
                                        __yy/` _yd4$PA_ggd$$DNPP_______ZlLLpauu.pammLZ7$kWT5TRP7TF5$rF``  WdfF57TKWW41F   +jj$FhaadKFCLW/___a/KC$W/KCL___Cwv/fC`5_qua#FF_yVKC___uaam#PFF__5wmnd$PPP______Wd$MRNNMRN#mmmeeL___                              
                                `     __yax/`___d4PPCLLappm+______.aaagggpgg#hhmVPQ$hkWRNNEPPPTP` W7TL.__y77TDWP` Wdf1L  dSS7PhWdPFCLpW___ud/R$UV/Fh\xAuyW/KC____aa#PF`_y/____aad##PF___.gP_j$7_______ppwMMPPPNTNNNNNNNNhkecL___                           
                                     __yV/F __yddf$$kaamKKZ$Sawwwm####KKNDRKCZZP5NR7PNNNBRRPF``` WdQPk\LutC``~fC__Wd7FLW\qgdfFNVZC5mmK__uadfCDV#PFLW/Z$VKCC_aapmw#fFC__y/__aamm#PPF__.agmKLLgj___gqapp#PPPT$___ZZZIZZTT7PNRkkLL_.__  .                     
                                    __y//` __jd4PA$adMRPRNW++#____IIIII$NN$DhmuL.PR$$RRMPPRKLW8sLWX4CF\YdD$FW`TwweWd$FLWW\TT`WW$$WVPF5_WdfR$NVPFFLW/AGVKFkudd#RPPP`__av/CuWd#RPFF__uam#6$Pk___aVmANM#PFCL__aapppuuEZZLZZZ77NMhkmp-__                       
                                   _yWd/ ___j4lZADdmmRPL_______.aawwmmmmmHHNRRhhkKW7PPPPFF``\sPAL.`3\Ld3XQZFW~fd#fR3$$LWW\3rL_J7qd$KwWamMRRMfTFFWWdAU7fFWWdd$$FF``_ag#FKWW4RPFF___ad/R$D/F__agdfNUMPFF5arqjpHNNNNNNNhLLLLZZ77NNRkLL_                       
                                  _y/4f __yad4ACgd9PPF5SuaaawwmmM##RRRRRRBTFFT7PPLW7FFF`\CL`3TFF~~F`\\VPA\xLL``87`Wd3$LLWd7$bWdAN7PPWN$PFDPTFT__WMRNV$FKWd9$B$FF WWd$FFWdfPFFF_uaddZC5V/F__jjM$$NVPF__JfANIZRNNNNNNNNNhHpHWPRN7$$kLL_                      
                                  yd4/ __y/d7Z$$VPPFC5WaMM##PP__________ ~5SCZZZ$WWRB8LL8sbWd$LL__.``3+FP3\\L@.AX8WQ3$FWW389VAAWd$PNda$FFWK` q$VMRWd$FFWWVR#RPF WWd$$kWW4$FF1WWd#MR$WV/F__ad$$$NPFL_ W4$Nd$$PNNNNNNNNNNNEUDKNNTNN5$LL_  .                  
                                 y/4f _yWd4Z$$DPRLL_gWdPP7TTCS....__________ggg++P~@P~;F@9FF@#+KuggL````\`7l\Vcc___j97FWW4P~```\7TRWd7TFF`  qqVPFhWdTELWdTPT7`L__dd$$kWdfPFPWWdTRT$NMRKWWaddm$RKFL_j;AN1Wd$$LDZNNNNNNNNNhEELWd$NNM$AkL._                   
                               __y/ `__y/A9fPPKC5aappPFF____ggggttppaaawwmmmmKTTTFW88DRK88GC@``\WmmkLL.._~+f3fFk-C.2Z`_ `\\GasddTTWdT7R\CL  \7TFRWd7TR|W7TF`` Wa4W7TPFW4TFF qU4PW7PPTRNWMNTN$$PFFWW4;PN1Nd$$hqqENNNNNNNNNNNNNNNNNN7PR\L.__                 
                               jy/  __y/ANI$Z$$kWd$PP_____.JZZ$$Dwm##PPRB$NNRPkP~~##~~PR888sLL.22###kwwmWd3T8$RQQbmmmecL_``~~\8``~3d$TP~\kcu37TFWd8TRR$V/F \\ d9$MRTFWW7TkWwqdfFP`TTTWd$RN$9RRFF5Wd4LWW1N4PRRN$$EZNNNNNNZEEgPHNNON$EO$kk__                 
                              qy/F __j/A$J$mmgcp9PKCSLaaam+Hjh9MMNPTTCC5ZkKE$DKL```````F~s@~~~+eKCZ````9\~~~38bWWQQD@@hwwwwwD88mL`Q7~\C`7bWWW3$R@7RT8d~~kLW`\$dd9PP`5WWTF~\dd$BLL`` ad4TPRTTPT1WdMMR$LWWd$TPTNq$LLDNNNNN$$ELL___W4RNU4$LL__                
                              W// __W/AAjZPFN$$PZ$5wwd##RKCDDPPEB$___ggdfNkkPPPkWW@smme@@8KC`7`55\sCL...`33.339P#9+KKC22@@~~~+++--480DW+R8CWW3ARq;g`_WT7FFWWd+d#7FR\sW```W773$F~L_qQ7W#TF`TT \$d#PP#PFWW77$VWWA$$NLpNNNNNNNhbLLL2T55MM$kkgL._              
                              V` _yy/f$N4$ELD7K_jgd6DPP___ggp$FF___paMRFRRBKFFF`__.3BB@@@/F~~~so@@9bbwmmm@am@P8``7`5~hmmu.C`______`~~__`59+k/`\\q|Ks.P~\sLbWdT$88FW~\s.`q|``3TR8WW88CPRTLW`` \TTTTT7TFWWTTD7  `Tf$$$LENNNNNNNhhkKuWd$N$DN$kL__             
                              j  j|/ARNdZ$hkZ__aJZPP____.J$PPP_S$ammPP55$DPPPF__samrF~@#SFW..28~8888PPPP9938c5.a.`````P~~+wwwwmwwwwGG... ```____3$P~\CQ2/hWWd888$bW@@\-WWa.D7P~~~~~5$WR\y.  .7T7TF~+RhWd4RNTL  `TTf$N$EpNNNN$ILL__PR9M$EN$$\L..            
                               __j|fP_jd$PPj$uW#AKLCGaam+#~fC5aa##FCC5.gPFF``_aa##RCL@@P``h~~~.``33.-``_..``.z~~~.   `````V#######~+++~~ \.. aawdtC.DWXs$D@~~#f888cc```~~++s/`\\T`j73WW4$L  |j37TW``55d97P5~~  J77TT$$$LpNNNN$hppLL277$$UZA$kkL_           
                               _W4ZFLW4$PKuuW#KFC5__WdfTC55k W/T``5 g+jC$.kLWW##F`5\Wcc....`...  `/`   agg_ sEC``___`~~  . ````````TTT``W3+WWdfF~~+ssZ5R+-_```T3fRtg____``33iL_~\qaZP~~~fL `q33/A.x88888``7`__W````TTR$$NNNNNNPPFkkgg_j$EENR$\LL_          
                              _jdfFhWdd$$uW#PFCLWKqWJZFEggcC____../KCS$mrKk@#KC`L.g~h\F~~--_-si. ```___44$..`~~--w-. `` -/`      ___`   W.`__`--``T3axc`5$.._`33RR$$ssL.../~A\..AX4$kC```  wd4+F@7RR388~~WsaaaW__   TTT$NDNRRZZIILNKL__A$CZN$$\LL_         
                             _j|TT$DYKNjV#PFC_grKhWdfRNWK____..wr/CGam#RFLLSCCkWmxK```````WvF~~-..  qy.`#~sE```````~ _..`-   `_------ ` `~-.....   ``~\Wwmmme-@`~~39Mmmmv//``3\F``3f$+-  .``3T`5`I.3338883\d9Rhavg_  7T$$RCILgggggWA\kLJA$iu3$$kkL.   x.   
                             _||I$jJTNU7TC__apKFLWjI$L____aaw##KKCWW/PFF5$mmzh@PR`k.L_....``__`.. ``atc ```|   .  .. wv/`______`` `8..   `  ~~~   ``````3f$9##K. .7TPTPPPF   ``_ ```T`` ---Wd`  ~~-qT~~~~`33T833R$bW  TTT$$$mm4EELL225+V7A$VZNM$kkL_   \v  
                             jj|$qjZLWJZ$SaW/PF___J$g_uuaw##FPCL_am#PF`_ggpKRKF```@~Ls.p...`wae/LL.pd$F  __..__.  +-_``\ aamwwmm.   ~~       ``        .``` ``~__ ```````````  --  ``   ````T`~````3I.....7`\\77B3fP   dd$q$PNNNhhmmwZZ1W7ANVN4$$ELL   `   
                            Wd4$kq|FWW4$ud#PF__aappAquV##K$$L_uam#FKCLWd4BBDPKLW-G.`WseF~~- WXfFWW/P@`F  WdakW-  ``\W/` W4#PP~~~\-  ` `  `_       ..  `\..`    ....        .. ```\..`..  ..aT0`` .o++--qsmF``38T87``   W7fN$$ZZZTNNRNhLZ_7R$$P25$R\LL      
                            W4fFKdlLL_j$M#FFLWdd#KL_W4ZC$2apKWWfRK$DWWW#9RkFFk-c_g;L@~|L``` ``ILL2$L.``  ~~``~` .  /~~  ```   ``2l    .  ax-     3s;  `3+       ~+     _  ~+u    q+~~~-  ~s````  `````33f$.-W`8888888````TT$$mELLZZZFHAqeLLJALU77R$\L      
                           _JJ$$Wd$kkud4PFFWWdMPR$LWdOAhm#PPhWdRkk##KKL27PFF`5\kwaxL`5$bax-  `js-------- ``..``   ```   ___.   --     +  /`       `    /`      ``.  `     ``  -- dT ``...`--``- ````.-+`T$...`33888888   WWT$$$hmqppKP25$gWZA\VKC24$kL     
                           Wd4$kWd$PhWMfFL_W4$RFDhHgggPPPPC5LZPPPF_`5k~P~CQ.WW4bW#8kWdts##K .d3$8D8FD\.`_  z;  .   ws.  ../-  ```    ``          ``              .         .  `` `1   ....`  .` ... ````.\+~~..`3388@88`  W4T$$PNNMPLWW44N$LLZ$5agZRkk  \  
                          W/f$$KNd$LKIZP$WWdAPPNWZZ$$$kk _qapPF___.../`C5pKrW@8LL_____$s./___a9###~___s.. asL a;   ~++  ~~``                        .    .      `              ___`  ----  __.  -.-  ``````.....33ss`533   WT$$LZP$KL__7f5$$LL_Wd$$LLL     
                         WWN|$$NWd$|Wq:Pwq4PRNILggggPRPL_WdfPL__ggmmKLwaePP\W/cSS--aaeeA~LL.27/F___\..__jyP+- -+   ``` _``     .                         +                  .. aa..  ````  uv. `Q.`  .`` `..~--3338.oW88   Wdf$$EEDPAkL_`7T$lL__UA$kkL     
                          _jjyPWT$$|WN1LWd$FLjggdNNTFF_qug#FFkwqdBRRLLW/CL5./`@@/hyW#8FE`.W~/``_...vttC.2/`````__      xu.                      .--4|.  ``        ..            tt    .  `````  j:    . .q.~``TTPRqs-~~88   WT$$$hkPRNqLL_9$$kuLL2J\\LL    
                       `  _|7TC_Jd4$LN$iWJ1hWZ$NNBPKL__Wd$EkkgWN$RK$pkKF\WgcL_ggL..PQfbsvrK``` v++o `~++mG    vx.      A+Y`                    +-` j|            v--      ..  . ``       -- `   `l.___.  ~|_```\.`338``3\o  W7T$$ElL WA$kgZ7PRNhhV#A4kL_   
                         _j|/ ___ZZ$|Wj$LPAjI$NgPFF5yrWd$Rkhh$WPPE5V/FLLzL5$kW.Gbe-__@038EL  .@``$L  ````\\ .W/~~  q.____                      `   d$.           ``   .   ++  . ``     ..Q..  .  as...  .3l...Wo----..``X\   Wd$$RmLL `1NKLLZZIIPRVM4$LL   
                         Wj|. \4amdj1Kd$:KuZ$N$$FF_WZCN4fP5VPP__$W#PFLWmyk@R@vFW`CCW.@@@9FK ___. /` __-__  aYL___  ~+---                    ______  +                     `1  1  .   __ .ms.  .``3+ms...--+~~.```..aas.``33  Wd$$PRAkL_`T9$buudZZD1Wd$\LL  
                         Wj|; Wff|Wd|NNfFWd$$PPP__j4AkMPK__l__jppKFFEL_Q$DLDR/LL`sso~G..``` `..  `` asswv.  `\y-  `````ts.                     wq.__` __  `         . `      `  ax     ``3$ W    ```9+~``````...`3o9P~~..W3  W7T$EPP1kWW_771NN$$LgZL23$\L  
                         Wj$;L T__p4$LPA|V4PPCCCLWdfFP__uammuam#PFL5ppaaxPFF``L..2E@`9xE`__  s:L    jj$PP __```1       ++~ ____                 A\vv- wv         wvm\     ` ____``  .__         ____``  .o.uoasm@/````...qqo WW4$FKKC__X\VZT$RNq$EhmW23$k  
                         W4fFk qqipR$LL_jZ$$kquwwm#PL__aWd$$WMRFFLWmpWW#RKC..`~+nss.-``__y. _`+    .a$/`` .x       ____```  .-                  ```~  `~ ..      ````      --v...___Js..____   .. ___   ~`~WV3P~-.``.~~o.qqy WW7$$PNhmc_2jNVZP$N$RNQNN4$L  
                        WW|$$  W4$FNAmkWj$PPjjVPPPF__axAA$$PPPF|__4$KKPF`_giLL``D3MKL._Gaxkk ____ WddfF   ++  _..    .. __.J`             ..             ++   _____   .    ``f+hvvwWwm+KL. .      qs..  ..__``.`3\asc``~~\qimWWd$$LW`f$K__JA$U2$$EDNNQ$$kL 
                        _jj$k  W4$$LZR$U4$LWdJRKC_S.W/T59#PFF`_SapRRkKLLSamAk-ypW/P\\sWdfFF saaxp W```   ``` aamm   +++y----  ...      .  ~              `    a.  .          `` `Z2````F~~yr   `  tam-- oox..-- `~~t_..```jf~ WdffKL WqqaiL_5+H4$$WPN4#Pkk 
                        Wq4$LL  X$$mpNqMPRLWJPFhagm#KC_W/``___gd#RRRFFbW##RRLW.PK```tggZ``` @###F  ``        /``\   ``` ```   mvr      +  ``         ``_    avm+      `          -mvw .  3ZL    __`3$L````~\:``_.`33..`  ``T3 ````\__ dfOAhVZZDA$$LKN4$FF  
                        Wd$$LL   j$$LN4fE5WVZCLJ4TFC5ap/F__aamKPRILELD88CC`@@m+F__---a4se.___Z``        . - ``      __  --  __``_____  `                      `               v ``2l `;  -+- `  a..`` ..-..3$--oam@P~C_..dd33~Wq___|__JT$2DhLL_d4$ELg4$K   
                        WT$$$LL Wd4$$WJ$kWPPEWWdR$kWW#PFkWd##PFLjpFRLL.SikxcE3$LW`.W.Q3$~bWax. `          `      ___../Q$$b wwx  `-..       cL_____ _______._____ `   ...    `  __y   ` ```     o~~```jr~~q.Z`@/#~~``uam-W\Q. W\\______d4$MD$iLWdA$kNj$F   
                       WW|7$$Ek WJ$$$LdZLU$$WWZ$PPCU$$FLWdfFFFLLJPK5pmmR@Q9kkF~~~~.pwaxF`@@#tF  ~~     .         aavm~~j;~   ~~ __y~~w    v +------ awwmm----aaxe.    ~~~   ......ZL__        .  `   yy   aqmg__```.WWf8```\:.WWqq___jVWdfNN9AkKU2$$N4Kk   
                        j|N$$$LLWWAf$LJhhmnNmhNRFhWd4RkWW2PFKGVeKLbxPF55$kPF`L```qiL```CSx/``\ ```     ..  J\.. @@#KC W4TC.     4$.P` `  `  ``V```   `PP1U``@PPP~~    ```  +yywwm++L_..__... .`____ _j`  ``A\s... -s.``  ..33~ WW\qq.gjCZTIZZI$$Wg4$M$FL   
                        J|7d$$kkW/`T$MFPPTPPI$IZLWJ#PFkW++FC_gXC5WPC55amREL__y// @1F``qqgeELs.L  --   `~ W `A+mm/``   ~`~\r     df+~     ....   ______```   ``_```         `3T`````~y+wwwwmoos.....__.._____3f~sL.``\....qq:B`  `WdtiLppuua$mmmmWd$$$$K    
                       Wd4447PNNYkWdTTF____5aammwmKFFC KCIDaKCCDPFCSWW#R$\ksxc___``___33$FF@~+~ `\y@   ``   ```~~ ______ ``L____```      ++~- .. ----    ```                      ..2`X ```  +++++wwavkW waa//Fhooo.`~~~~df$Boo WW7d$mLLpWdRNIPNjg4$$Kk    
                        WA\$$LL__L_JT___._.ddfR##PFL5._qapmRhbKKCLgg$KC@D#kR6bk--``-qg2Z$FF``C````Y0       ___ `..a--wav/  w--  2i      ```_     ``1          Jt  . `       31   q++~   ....```````W9fFW~~HtfL ```~~.`3/```~~Y~ W\V7T$hqgPTO4$LLjgQ$RK     
                    _    JT$$mmnwkW/__axrnyP__5$TK5arKuW4PFF7`C5ggpB$kk###FFR+kLLp WdaeE/`` yr    xr         . wWW``@@~+   `` WV#AW44m-- u....__    ____      `  ~-              dT`\L.wammm ~     ```_  .``FL..`..~~~~~__``.3  W|| 7TNqlLpWA$hqmmm$KK     
                    4.   WdTff$D#KK___2T$VZLL.pACuJ/KhW/PCL.._aW4BBMRKKBFF```$bmkL.Wdf$EELLLZLL..``____.  `   ````    `` __     ````  `  ~~~~wv      `...  ..  ..`____  _.____   `  wvW/`f~\  `    ax......``__y---`...`../+\.. Wq|__ N4$kKL_2$N$RM7FF     
                          WTT$$ZF__aaiL.__qampPKjV/FNVXKC_ggppmBBBRRBPFF~L__@@###k-W``$$F@+---uxr `..aax             xv   v              `````~       ~~~  ~   o+-wvv- ae- ... __  .2`` ``....____`2~~~~~j.__a3/P` ~~~ovWq``3s  WjjxL.Wff$bWqg$$TR7TF  `   
                     _______jjf|__gd##kkuuW4$FLWJZFL_____g4ODRRRBFFR8TF``--o/``````.`33$F```````` yr~~~~   _____     ~t.@3r                      ..   ``` -    ````3fk ~@@~Wvm ..  --    wwmmmww.--GGGE-u3i.WdtCL___..``__y..g_ WJ|$m;W`TILWj$m7KQJKL      
                   __..a---`JI$._qgZP`T5Vggj$LWg+FL____aap##RFBBDPF```L_``88kk....-g.33$L..___.`../`  `` ____y--      jr ``                       ~      ``        ``   `--``_ ~  ```    ``33P ~~~`@++~~W3fF~`$$  aav-``-./|qqs.Wj|$B$kWdq$Wd3fKhV/F       
                  __yy/##m~WWdAwqqmLL..2Z$$2DkWK$Fk_gapd#KFFPRRP/F`_jssoz.@/F___~``gggZF~~`oxx. ~~         ygCC_.   __   _   ___   __                                    `amwu.   _______  ``   `  ```` 37``___j.W@+~    |||3d+mWq4$ZlLWWAqqjJ/KU7FF       
                  yygZC__``````RXN$$bppAqmntfFPPP_WW4A#PR$LKKDKF`` Wtgggss..L....`qy8RE.`````X\L`. .    __ Xt$gg___________        4                        _            4f#~~+   ------     ..    ..   ``  ...zr.```....`qqV/``Wd4$E$LL Waam/FW7/F        
                 Wyyamme.._   ```T\4$KKD$TPRTF____W2Z5TFQ$RKkFF`  .d$$EF@g/L@+~~~_Q2ZF~~_..    yy________.__j$pk _ygss--__________   ___         .           .           `  ````  ```         -  ..3+` .... ~++f$L.    .~`33r`` Wdj$$g$L_Wd#fFkW/`         
                 W|fM9R\kLL_    ```TT\\am1KN$Luaaeu$DkkLj$RKRTF`k~o@33$W@8CL```..aa$$F` yxL_______-------- y4/P__yxm+~~ggggg-__..____________                ~      .                        `  y._``   ass ```\\\____.```d3lL   Wq$$ELLLW77TF //          
                 ||TTT7R\\LL.     ```77$$FFqj;Wd$$V#PFLWJRKLD\k ~~~`03\ba8kkc~~~qd3fFL__.`___ggzgg/__Wf`K__2ZCL-W//C___yammmkwggg________________            `_    x+                           4C   ____``  __``\..../ o.q3$s  WWj$$RmLmy/F`  ``          
                W||P`TT73$kkL. ``    44TT__5$$KWOPFF`_WafFkkE/L```.os@@@38Fh\.``2ZZ$C  qygggaxmAF``WW/``uaamwwwW@$GwwwdMQQ$DL______ggsssggggg.._______    `        ``                 ___         ___yy..____....jjyy~`..XqQl.  WW4$$B$$NKK`               
                W||  ``T77R\\L__ \cW``TTIuaa/PNVf$____V4RKDDKFk W/@@PKGG3ZL@`--uy--~\ _qispW#PRQLLwWX~Gudd#RRNN99#WW###hwvmmwaaaaaammmw#mqggppccpx---.         .   . .       __     ________________./g__________.2..L___`.3+-  WWd$$BQ##KK       `        
                J|1   jjT7`R\\L._`+~  ~+~~ffF____2aaudZBRR8BFFW@/W@8PGo8#6kW``_2Z`____gdamWR8GGammmKP\WW/``________________999####RRPPPRNNMMRRkkmmkk_jL __    y    +~~     `\________yyx_______..-g______ggggggzggggg___.._`I.  WW4$$$$ZEF                 
                `||   qQ$F``A\\kL ``````77T`___aadd##NRkKBBFF`WXCL@--W888$Eb-WWdG..uaadMRRB@@WW#PFR\ _______...aaaauuuaau...2ZZ7TTTTDDLWW7fPPPMNRRFLGxkW y-  j___ ```.      qqs---__ygg+gggggggggggggggggsp@w###w68Bkaaec-__3+  WW4$$RR$KL__               
                ||__ -\j$FWWW3$\LL_.   \q__aaamdARN$PPR5RR/Fk .`\s--W.am@Aq@.@XtqsmWd#PPR5588#7`` ____.aaamwwm###~#######+mmmmeP`~~~~~hWW``Z_____`\WW+KL`\kLu3$kL..gg;      j3ss~~vv/A6GWXwddBBBBGwmmmmmmEbL@@PPD@@6@@8RELL.__  Wd4$$B7R\kg..              
                qi.. `33$LL  `3$\kg/   X\$am+#R$PRR$KCD7Rj/F \;W`/``./A8-8q\-_`3398WR8FL53s8.______uaam####PPP``````````TTTPRRRLL`````WX\Gamaaeg____```WW3bWW##+~~yvR\L.    `77` WWMQQ@WMNNN6RRMMMMRBDNMNRMmkkcLgZQ2W88DGqsgp.  Wd4$$$TP`MMbk   .          
               W44$k _j3$kc   WQ$kLL.  `7ffT`57TTQ7RhyKCQz/L 3iL.`Lg````--d4$bWW3ZFF3$hqye~~___..aw###F```_________________```\\\_____ `~~f##9Rhmeeg___ @@@VP````D3XM6b~   __|__..i3Q2Z```7TTR99NNPPRR#PPPPPRBbbwmmm#@~##RR6bL  Wj$$$RKKW@8Nkk             
                `f|__yJ/PA\   X\$$kgc  W`TI$aW/__y/_jZL@zRkWW@Ak--mqC..` .q3$rL@3.F-``-3IEECuuaam##F``_______...uuaau......_____\\sg..___````T`75RbbbL. .L..   .x/`0YF``   _jyggggggais__________________```T88P####KCC`3559$EL Wj$$BRKL@y/PF  `           
                 \\..z/F _`_  `jff\EEL  `ddf#KS\a/LqJ$LWZRLW```````Aave. -44$kL./F_``.WdGSmwWW#PTF_____aaawwammmmww#mmmmmwwwwcL__3#hmmu-_____a.ZZ79RmbkwwWw    .` ..  .  ___jip##R6W@@jaaaaaaamwwwwuuL.._______````T\\swaaZ3$EL Wj$$$DKwv//`               
                  jjyfCL_______```jjyL_ ````\ Wdj$ujiLVRKFF__`-`--.@3PF~```3$9~+R..._~~~+PP`````___uaww#+KNV7PCCZ___I7R$QPPA\hxvL_`79RkkuugqzpamqZ7RR\KK ``    ~  ~  .____.aamRRR___SSDW#######P##~~~~+mwwu.._____``.Q33sBQ8#~~ Wj$$RNNN/F                 
                  j|$$kkqgge-  u.____L_. ```3Xqq7$VZ$NBRKKk@./L@`pWg/``   `7ZT``~++K...ZZ____.aaaamm#PP``NW4$kwaxuuwrwd$$KL `7f\bvc__`RWW66amMRRamLPR$$L       `  `   __qggdBBBRuuaam###T``_____________P~~+hmuLL____jGGBRa8F` WWd$$RNV/F`                 
                  j|rFA\Wq$EL__++wwaampL___p/A\\dqj$DRKkP`Wj;F\s.P`\LL____@/A\s.```~\++mmwawwwWdQ##RTC`  WdQlLW9AkVPFL_3$DL  ``TfAKuL.._@@@9#####t|Ld4$KL            __qd4BBPRB@@###FF`_____..puaaeuu....ZZ27P\hmu..._I339P$L~ WWd$$N#/F                   
                 W|fFF Wd#$kkWd23WWd9RkLuwx/FWW4TN$$LP$LF Wj;L@arL``sg----.```~   ````3399###RRR$CZ``\   Wd\$kZZ`ZZ`__a8PFF    ``T9XXmqq.@##F~ _jj$kW3$N\W           qqdZRRKFB\VP```__a.wqqymmmWW@@hHmmmpwwe._279\bkww-33Z8`ss WW4$$V/F                    
                 W||F  _`3$9XhmmmWW7RR$VW#KLLWd`Wd$$kk\LL WJrL@@\L 33pF@WQyL ```     ...2P`````Xq$$L___   `3A\hwwwmwwe#PF`______l____jjjxv/  __jyy/KW3$//            WdfPFP_____LLaawW#~qjV7RC____.27$$$FPR\hmeLZ7$RkW@@##B@8eWWd4$$$K                     
                 4||L____y7``\3$PP```33#FF\\.W~ Wd3fFk\LLW@fFbsx/LW38FL__j$L        `Xf$.``..  ~33$bb--.___```#####PPF``` ..-wxwAAKCC233PFL  .gddfFFW3$F             W4TFL5wwwmwwe##rF` \q4/KGGuuammwd$$k ``7R\kk.ZPFW8BFR8B8FWWd4$8/F                     
                 d4$L  aaZC__.``    W377F j3rF``Wd7$kW$FkW``53#6FW@/P__..24-_        `TT\qgg~_..77A9Mkkwwc.._`````````   g~~~```555~~~~`$$.W~~Wd7PFLW3$k\            WT$Dwxc~~~f5TC``   W4f$W@+XW#fFhd$$kk  ``75$bkKL@3Fb@a8F`WWd$$$CL                     
                 `4$vkW~fAbggg_    .Vf$` Wj|FW33W7`$58RELL.sg@@8EE`C`.ascc``L  __`    `T1X$$.w~+```TTRMM@hmmk- ...   ..KK$C..-auw-`````5ae+K`3MM8FF ``7`             dj$g/AKGGI.a$u..L  `T\\LZZZ_``__2ZPFL  _JJ77PFkWW`GW88RL.Wqd$$4\L                     
                  `\$|. `QQ$Q\__    |j$  W|||W//```T385bmW@#RG.8AWekWWd6Fk~~s.  x-      1ff$VW`IL__``~~YV7PP`WWm+~wwmm+#+++~WwWMPR\__aad/RCWWd#RFF _sZZ`__           W4$$C``~~++##++hmm ``3\+mmwwwwwm#PF`  uW/ART$CDPF@@W~F.~~qqj$R4\L                     
                  `jj|._  3$q$kk   ` j$.LWj|;L``_.37`~~PR\$Lgggg@@\LW@78FQ.``\  `v       T3$. -+ms..``3I\```__````````````I``_3IlL..aa#4QDWW#PFF`  qyFFssxL__        `3$$k  ```IZZZ````` _```T9#####FF``   /`__33$mLF_..`___``Wj$$R44\L                    
                   Wq$LL_  ~jjyg__   jyrkWq$;pwwae/~```I338bqa$L--`\L..``sgW`\L.@/        ~f\_``9\kcL.z~__ggg_.._____________33awaee#Q8$$#W#TF`   qj$F`@3\\L..       .22$\\L  ~~yymx-__ywwx `````````____..SSaad#A$KwwxKu..a. qjfFF34\L                    
                   Wj$$kc.__I$$kkLL. 4$|LWj$$PW@8TF`..g~~+~~qQ8bL@@szg___``N`@e--`   A   ```\a...`A\+mwwwamwwmmmssussssaadmmww###88BDa8###F``    .33rL  7P~~~~      vqq$PAX\WW`QDPPR\L22@PAhwmmwwxwwa.uwwmmwWd9PF@71P~~~~~~~~WW4$FWW4$LL                   
                   `JT$$eL__y/#hAmvg__$\L JI$LL33iL--sC.```33$$Bb@@@AGLq.gE`@@/`    ``     .3++qs.`3$8PP~~~~#99M@#W##m########8B@8.n#P`~~` ``   --+`\  j.C```      `|33$FFA\xk~~+600Amecg__````PP+P##+VWfQ5S$3ZFLs$$F`` ``.. Wd$$P@W4$KL                   
                    W|TR$kWW/$F `AXKk.2___`f$-W##tL@`3~soo..d3$B8R88@@hqsEF@s/`_      ___  /```31k-~~+$````TZ3I3PTTTTTTTTTTFF3~~r~~F``````.    ``````__giL.      +  vdQ$$LW`A\CC`_~~#R$kksug._______`I__I33m#R$LWa8Pk  .`~q. WdfFF`W3$KL                   
                    `||7R\VWQe_  ``\XmqqiWW3IDK`SS----`\.g~~d3S$FLszc_@@3\k@sg-_______jy  `   ./``_``I.      y+-       3sss.. `````       ~~- __  .---y3$kkF    `` `11j$y_W``3+ww..```T99Mmmmmmussguuaaam##KR$$mW#/F`  W `j+ W7$FL__4$k                    
                    `\|.`3fRR\LL  ``T\\N$LL`+~c.ss8#`..qzcp.Xq3gLL.Fssa8QDFP`ssmxk-..w3rk  _  ``   avmmm. ```T``_ ..   39P----        ``_````\ue..``.Q38#FF         `TQ$ELLax/`PX\v._``3TPP99RRMMMMm####RRFF@+#AKCCL  `|.```_jI$FL_j3/F                    
                     j||_```R\$k   ```33$kkW`5z@@@ssooWd6iW-qG3mmm6@@@#ms8LL@zs//` ~~~j1      `__  jfP~~__   \$-  ~    ``````          .. ` ..~~~s..3d3$F`__s.     ..3df$bW@A\L ``\\...```````TTT9RRRRTTF5sW``Z$aavk  ..._. qq$$Egqjy/                     
                     d1$L___ j\LL`\  ````\\Lpp#6@P`\..@@3$9PWVfF599WVC0@9sFF@@6F______`I  z/    .  ````     y7`   .                  __________```+~~_j$__ wxr    qr~`3$$Qy@/`   ``\tm. `___.```IZ2;5~~\samAwaam#/F   .|..._Wj$$bwa4/F                     
                     `ff$Lg. `\$LW`\L  ``jj$s/F`_L...--d3PP~``SS-ZZLj$g@23FWW3RCyg------kxeL   ~~  ``   ``  //    +        `         ..aqa-----...``..3$kWW/``    `| _j33$$L.     ``~f\  w.as.`\ame-___33rF@@##FF`    -||.saWd$B@@a4K                      
                     ``\$$epWW3fkW@wWmwwWd4$ELLsspwdsL@@36GoaasW#GEu3+sgg/FWWf6qxC@``@@E/`~~   .`         ./`    ``       .      ..  /+9fRQLL@yAv-L.ua##P~___     41wavmm3$bwW     ````  dfR\y /~~`C...//RGmv7```     `|li-Wdd$RGQ3/F                      
                      `X\$$LLW3TF@YP`~~~~Wf$$rWaeFF@AhW@A8b8@#8bW3mWdAS88EL.@@PA\kv-@@+AG.``--mmvw                               +-  `.``\j$gs.@@@@WM47F``...     `~\ff6QQ$gyL   Wv  ..  ``_3. ```wwmm+P--~~~``        jj|__j3fRaa//                       
                       ``\\.L_/`L `  .7/``\q$LW7ZF@``Q3;QQz8F`G@@~A\y@RrF6bWu`.``$X`L```@sL ````~ `   wu.                `       `  _j...w3xmmsL@_@````` wmmc.    `````\\Q$$yK   `\Lus.  ..aa.   _/fT$C` _```         |33\_jyZG@#/F`                       
                    ``  ``\\iL______yg~   Wj$|L`s.._@@+oWo8P-.88CCQQ$;R$E@@@~~\qa:Fgg___`\-  ___`   __~~    _ .              ______.jyipWWd89RAbkwec__-_ @PAk..  .....`.lq$$EL      ~~~  ~+~++  uaxZ``_  ___    _____yysRqaamKyy/``                        
                         ``A\xvL__ --C`____jI$LBskks.28.XQZLL..9~~Wd88b-kcL...Wd6$F\Gae-``\L``      -- `    yr   ``     -   __---g-gd3BK@W@PF```RQ$$WA\L.`` NxL  ++mm-wvdd3$$kL    ``` ..`````. J3++v v- yxe-   -----338dWd#RNj/`                          
                          ``3\\KvL_________J3$FFRcbaggs;qj.gaamrF`VRRQQggspnsvW@RFU@M#Fk ``~x~ `_.  ``   ___/`           ___yy`amq@39PRPWP`~.```~33tL`5ssG.WPA\L.````|||`Q7$R\\L       ++   --  ````  ``_2```  ```\ydd8$W#7F`34/                           
                      `     ``3\\KwwaLuuaasd3IFL@@W@F66FW3iWW8RELW``5aaenjFP3I.2``W38$LWx/F`\.  v          .`         ___yaddmWWQQy##FF`````-  .``$$mw@7Qy/  `\jy.`  \...3388M\k  ___ ```  ````      ...a.F`     .yddQBRC``__j/F                           
                              ```~~#+++H#6mmPFFg@g@RG88LWd+~P8S$ggs.@#f\LjEF~~ssgu@38$LW~LL`ai____   q..        \   __yyddMMM8KWqQ|ZLL     ``__.__j.  `` `    `3|     +:.33$FR$LL   y        _       q. ~~L......ggd3BBRGqggaj/                            
                                ```````5TT$$LLLWssL.@~s._j$.``3sbuzcL``5XqCL``3$EW@P3$F_`-WwmmkvC-.   $L   ___      .gd+@d9PPP WWq$LL_        _-_______________j`    ``_j_j$.D$bWwk@/_  ..  ...  ___ j| ``--`~yyqddM88EP@84Q4$K                            
                          .              \j$$L@@##bc`@3auxe-W@28@9#EF~~o33$kW@@A$8\G3$LL`LW@PP~thbx  `3\k..a...    yad4$BPFF    XX$$______________..--___`--___y   _______jyggj8/F `C . ~~  ~~:  ....4.  ``..`Y|Q38B88GL@3Q$8/k                            
                                        `jj$$kkFFF@@o@@@#fFLWjs.W/RRC`g@d3TFL`.338@W/Akssc ````` \\L ```_~~+++~ . g__99#KF`     `TA\$LL________________yy `k W4+   yxvvgggy/Ajjy/  `\swy    ``    ~  d|  .....qqd8PP@89sg@34/FF                            
                                         Wj$$kLL@.g@@pK@``..qgzpF`....gjP``\.p@~~ss.``@4\LL`\.. ```      `T```  xqs$.//F`    _   ``3AhmwwwwwwmmmmmuLL_____    ~____  ______LLgy/L   qs.` ____    ..   `  .y.q.dQQ8FBQ32ZGa3/F`                             
                     .                   W4$$EkkssbsvP@~-uoWqa8FF qssqqgEC@jrKC.`3\kL..#A\k-~+-   ``  __ ~;    ``aam+KC_    y--   ```T#######PRRPRhhmmmeLL_____________ggipppmm/L   `j;_  ...    +   ``  ``../dQTFBqagqaaa//`                              
                     |        ``         W|$$$8bgg@gjL.``@+PHQ$LLWjfFqyxkkW/``b~-``tLz__``\L```  ..    . -- ___ WV7F``\v   `.``     ````TTTTT```TTTTPPRRkk--_______paaaammhkMRRkk   33$k Wv+~   .`\...` ... q|.3$8bgqGaa#PF`                 .             
          `         `     .              W||$$gggGL.zk_ssg..`3$ELWJICQ2gC5L``L``__yp-op--`  .`__ ~+     ____as.a2/`` _____  +  --   ____  ``   `` `TTT7DMMkL_gpaaamm##N9PPPPPFF\    /A\YL``C.     q++mo~~~~..+yQTG3aay##F``                                
   __                        `           `||$B$bgaaeKw@-kgsLW38$kWz~WdfGsspk-LL_.a/PAVP``L` -  ..``. ___yiuuz#+~F`___ .i...``\Y`____j..amk_____.     ~~f$RNaavwW#RRBBDD7TFF````     ``3$Lge~~v    ``_ `_.` .`||338gqay/F`                   `              
   ...                                    ||$BQ$V@8$LLz8KGsL@@8\bWsLW2Q9R#cL@sLgz2ZL./~ \.L....~ _____.y/A##TF`____..WwmmcL_ 2l.aaaww+rF`\L..w-- W/```II7RWd9$KN7PPRs#P~FF`\\L  `_.___@A\V/`` `   ...  v--`..|33qqqay/F                                    
   ~~~              `        ..           ||$B39$F@8bk~~@@+ss--@--+sWqyZPA\F-+#eeFgy;````~~osv-  ```.pzzEC7``___.aaecL`3$$kWq@+~@@~P`$C. wvr+W`_____uamrF`33T1P#+F5j7K```__j$k____yyyV/`\tL...    /~~  `````||;Aqqa3Z/                                     
    `     `                  ~       .    j|$BR3IL@88LLLWSCD3LLGC``~Wj$EL`````38FE@7EL  _.`3PF___jspxPAjyec .qzzp/R\kk  ~~~~~jC`_____jyr `jIL_i..wwvWPP$5.~jf$C```_y/     a4Tks..3$./cL `\yyg~ .  ``      ``33/Pqqj$/F           ..                        
                                          j|$P33$aeggbgg@ziL`.ua:k`.W2IEgs.L_@3g_gy/F--.@s-`___.aam/CC22$FF WqmmFF `jlL..``.`3.-uaiL.3/FL_2iuwAAWWMXCC`3xKu77A\\WW4IL_____df; ~~WwmmEF~  qjiLL@     ______./33C`q347F   `        ~                         
                                    `    W4|$BW38Q$b@@6k@esL@@W31kwodd$Epob---AGGa86L@wW@/F`uuwm#PA\\axrc``_`7TTF`  jymwwwxwWdxWWAAmm#P WWmmV/`` Xf5axm/`_W//F`~~~~+\y---._______39R\kL  W4xyy--   .......p+8`hqqj7/F                                      
                         ..               ||$BBqq3igg2QL@@8L@.W3|L@8Q39$FFFW@@@@~g@@_@@``` aWW#P``_j3XREL  -y___....3IC`__`L_2`__``T1P____________ ``5$\\W//   `..``3ggg;Lu-aaa-u.Z``lLL.23$$L_. Ww~~wwqsiBDD._ja4/F                                       
                         ~      v         ||$.R8386GaagpL@ggsLWqiL.GwdZ$LL`@ssW8ZSSg.._`` W3#F`   yV/`\\YL_..ikqgg_yyg______s.._i..`______....________ _____ ______j4$GG-WW@g@@@@+~Ww-yggcgj$gpcL._ ``W39+kWRqqa3/F                                        
                               ``  `  `   |||;B33IQ59RBbLgsspLWqsec@#Q$ggL._`~~g~~qaxLL  _/``5   jy/F__j\Lux+~________.saawwmmWwakwwwammwwwmmmmmeg-_..._______________#j$L03M4kEZLL.`57M8$Wd$$bkkw-- .d``I`__qjaZ/F   v +                                  
                                          jj$:FWd+GdTR$gLgg8KLW3$$FF_q3$bkk....Q$P@3$kL .___..  WjZCL../_______.aaaapww@@@@PP___``  VPP9YPPPPPRQ55bseeg_gysauaamwmmuLLL2$g__jf\\xve__y/__|Wd4RPFF~`~~++``.q.gd38/F   A1```  ..                             
     .                                  ___jl:P`33888Uq$gggELbWqsELL.338$LLL~~wa.Wd3$LL ~Gaax-  jymmwwdaaaaaaamw####KKLLCCIILLL..._____________wvMWMPkWWWQ@@##RRNM##mwwmKCL.____jSSkWxL_3.2##RR\F```````...qqjZ7F    `\                  `                 
        s                           ______../ .3d889qdd666FkkkW@96kWWW3$$LL..`@X+bdq$$.. tV/P  WW|$|N99#######PPTTTTR\mmwgg+wwwmmwwwamwwmauuL.___________________________h+wwq.____WdsLuamm6FF ~L     ____jj34$/      `                                    
                                 ______gaappk @888..d7RRBBEELLLW2PL5gg#3$kkkL_.``\3A4xkL jZC_   jj$.F`````TTTTT`   ``3RRRKCC227PPPP########hmmmwwwaauuu.LLLL.............2`__jjsi...@A#WPQQ$/F ~~  ......ga334/F                                           
                              ______gaaddfRKL `88uaad8QB$$Sagggp.F-gsLd3$ELLLy_ `\.P3$ELWjyL.   W4t|L_____``  ~~~...```55RhmmqL____``````TT`7PP########++mmm#++#+++#+#++mwuuu339mhmmLZZ5La3$KL ``  ...ygggga8/F           `  `                             
                       .     ___yaaa##RNN$$LL .m@@399AW99RR6$SggLL@@amWd8$bgscL. `\87$$L_3$k    W`$$L.ggs..___``.-~XCC````TR#$bmmeLL..__..  ``````````TTTTT```TTTTTTT``IIDaam##PPPPP++eewm4PF  _______g33dQQ$/F   `    --                                  
                            __yadf#RRDDNN$$L  ~FWG88``33$99###$ELkWRQ8L@3$FR6bcc ``./A\kWggELL  _`33+mmwmkcu..  ````\s.__```339RRRkmmmwggc_uggg_..__.____________y_y.ugaspWRTTT```TC57XQ37PF       _jy39#A88/F   `  `  ``+ `                               
                          ___yddTTRDPNNN4$1k  ```~~~.od38899RR$$LLLLaiL.33$88MkkW uxCD3A\iLgsx---`2``55999WMmkL____``3+s..__````7PRR99NR6kWWd6kwmwwmmwwwuaiuaiu22lLzaWWdBBKP``\yW/~~~ _jy/F       _qd39KKQ3/F  `+   `   `$          .                      
                         ___yd4$$PPNTNIN3$|L   _.o88qq8888q89d9R$kL_jgkLL33R#QQ\LWWA\V`0AAkk@FkWW#/```TZ2@@P`\qus;  ```3asL..```````7TPP##K#9##88NNRRk@@@mm@@@hmmmmw@@#R#PR\CQ3x/F```_jy//  ______yam#RQjy/F   ``      ajr                                 
                        __ydd4$PR$FZlUggd$|k  ...qz@p388Pq\.g`T7$RbW.ABkL@Z88\QLL.`A\\L/``$$QQ@WP``L~~~amsC``_W3+kLg..//A9kqsgg_________`` _```_~~~`TT```R9#9PP99####PF```_j$3/RCL ___j//_  ___gadd#PP\ay/F`   __   .  d4E         `                       
                       __y/dA$$FDlLpppdN4$|k  @.Aj$vPA888W\tqa27R5MgtL@AKyLR888kk  `33$kW`7A\$8ELuiL..`P~~~~ _7`A\Wmmmc.338Q$mmuuag.________________________`___``````S..uaa##PF\WWqqaiC  ___sidM#PP__yy/F`     ..     .``   ``                            
                      __y//PT$$DN$NHHHNg4$|L  sLL33tL`3\sd3\9aBPRd7PAkCL2gLL_z/LL___```\L``93fRbvmmks..```..agLL___j99h~~~WdfP9H#6mmwuascuggppax-gggg---_____________.zpwWd#FF```__ygd+k__uwam##PF__qa//F`    .ezs .   .                    .    `         
                    ___y//F d$$DN$NNNNNN4$KL  ~kW``\xud3oxP`33SSWdICQ$bkcggLy____`s..``jy___```\YQ$EgeL. ---~aameu..___```.|```7TTRRMM#6kWmmkk@@hwamcpKkgggggwaaappwam6BR#PF`sgg_uuW/Q$$wwW##PFFS__aa#PF` ____~--gs   ``   `              --+              
               .    _jd/fF Wd4$$Z$NNNNNd4$kL  `F@-_@AXQ@8$bq223qqdqamdQDkkqLLLsL.gzgL__7`L_.___________._`\S23PRhbmmmmu.  \vmmod8`dTTQ$BPN99RPFWWMM6BkkWam6MMW@M6M#RRPPF~~``5asb@W~jjaa###KC```GaaWd/FF   o...G3Q8Rk.  `   . `        ``` ```              
                   _jJ/PFkWWW4$$$$NNNNNN4$KL  `@8ku..A\.8ooaeeRW877T9R$PP5qgippmku~\--___gsg-_g..3axxwxLL wwm..`2@9999kkL.235zP~~~9+A-+-KT7TBBPWW99PPFUV#PP##PPRRPPPPFFC`____3$BK``Q33PFC`IuasmWWQ9#FF   ~~~~~~@ttF~~                            _         
           `     __yd/fFPCU WJ$$$NNNNIZg4$kL  W@@@@sL@3+q.P``5533XdCZ2I$LW4$$LLCLL@@sssiggsLLgssgg2Z#~~\L./`\+oamuZ.2/R\.~~+3ZE``````TTRWW4$B.oW077TC`7/`TT7TFF``T`````\yoaae@#PF Wq4T`` awd##KQ$3/F``  __`FF`-.8$L.` ox      ----------              . -  
     __          _jdffFFL___WdT$$ZIZ$$gd4$kk  ~~`.2ZLL.`\x..aaod3~\aqq$EWWd$$kkLgpL.@#mmwmmkkWg@@gsEF__yg___``~++h+mrF a.F`33PA---` .g~~~3f$88mq__S$ggcC2zzg____``_....asz8###F`__33ICL@V###PFjjy/PF  `Asy/```@~@zE~~W``      ``  ``` `              y; `  
               __ydffFFFW4a.WW4$$pqqgggd4$Kk __@@oaxho;``3\vd~~j```3dd$kLWd99RRqEppLWP`R9RRkkWqypAA$L-__$.x--_``.2Z`5L_@+-_j```\IL -aSSvw`T99+RaGaammwmWWAGGG.wqq__aaaawmm6G8/F yggg$SWW/L_`__yJ/F``WxF@jsFL ..  -F           .                    `22`    
              __yd/A$EDWW#AbWWd$$L$$$$ZN4$kk WWkc@3IB3\WW`AT8G33ao8WWdfhqqiZZPNN$kkLL___77R\8MMtKQQ$kWuaxrcLhxypwqy.-~K``_jx.___+s..P3PK``````P~~~#9###KRQ$##~HGaam#@++RQ$$#PK__.344EP@ESLg_uax/F` W~6\W3ZEL_...``.    .     -+             .     .es$     
             __yd/A$$kkPF_99 WWj$ppHNNNN41kk @FF~~gEF`~W````~qdd#888``TTTRqypWW7RRhqpLL..`W`\Wd$kWjtLbW#6Fk__y+F_jj;``qgsW/A\s.``jy/``.......`````77T``593PF``3W#+PF``533+PF__..id28$S..WqjyV#PF\  W`.W#fA\E@-e-_`-    .     ``     ~ ___        3$F`$     
  `        ___y44$$PPFLLLLJZ  W4$$$$$Zgg41LL sL.@@8EE``_ygg_`3T833338`WWTTQ$LL__25d4kkbp____99PPA______`$LGsV/`Luai.  jyg@@`RtrLu2/__jy-qoee___y~~~j.  ./```. ``3$$.w-+```` wwqqy+AjyyrKCGam#F``2/@@`_L`I``\88@#/`` . ``   .       ```----       j` `T     
          __yd/f$$PFELgpmq4C_ Wd$$$puqdd$1kk 6bW@@8GsL_Wdaqsp`~33----~``\dd4kuupmW77RN$ELLgg..`C2aaaaiLpmvg~~_yyWAt$LW3XAG.._`1WqsCLW4/``7T$LL./``jyc__``` ~~   y+~~``___.____j____3XKC_WW/PF` W/A-.@..as.@ayp@@`  ~~  `      .         `        `. 3$     
         __ydffFRIEEpaiDRN$bL Wd4$mMMN##RFkL R\LL.85ssW/AA9tKWWW8888888WWWff5HtLLL.__5$gggmmm--~++#####KR\L_.Wx/FQ7F~~~Z25\L..__3$kk_____`j3mmmL W3$FW-`__``____````_..3axcu...qqyp/A\Lg____  W48D@bor#@8\@@TL_`   ``     `- `              `     . ~+     
        __jd4$PPN$BBM#RbWH9HhLWW7#PPFPFT51kkW@@bmcc@@#KKQ23ILL``~~~oq~~~``T77R$bmmmupAAGbKRQDKLL2ZZIZ`$LWaxgg/P  `/C_.----`hssp-//`\\..uxu22PF~~ jjf`` \yy- ...a.---~qxrP~\Wg+qqazKLLpXqqi..   `@-`WMTL..s.84L.... ``__   `` `        -          ---`I.    
       __ydfR$LL2ZPRBCDBWBTFDL__ZZT`TT```$Lkk@@P@@@sZF`~~-@A+wv-```X\..`WddTPU7fPRhbKCO9RRhqLLkeywa+eC2LW`A\$L..__`_ssA0XC_@3$MK` __~~+#@@~`_``. `7`____j ___ypdfKK.Q38$``.X`G3W46Gux/ qjjiLL_ ``.```|_~@ss@@s~@ ..`  -   `          ````        ``  +~    
      __jdZPPFhbgFKS$pPABPPWM$Kwaeep   _j$kk@yFL.@33$L-``3.2`XXq...`\ssWd3`\W7TTI$7PhWWZZ_j$iKCLLLZ`5SxkW.Q3ammw-___39W@~hWd2ZF___ysC2`__....    ______....aa.RPC___y``__yy_qggf$9##FLWWJ$$LL__  s..q.L@@38EF`EL`~.````   `. __                `     ``    
     __jdf$FPT5IELWqmpKRBILLgg2W#$|L` __j$LLk.L@xW@RAkkLgg+~ `\axk__333o88``~~~9a++B5Nq$Lg22DFhqepL____LbwW/P$MkWjyyFr___239X6C--3frhx...zzgg_____.aaxww++~g~~_~--..________yaaZZZ5T` WW4$$$kL._  .WdikascB:L`Gowv--.` `.L`~~--         --   .             
    __y4A$$ELWd9PKKd$ELW9+buuaiLZ$$LL _d4$Lkk\L/`\..3fAWmCCL__W3Akwa//R8888883777TTbmdd$$kqgELU9RkbLL...._N$C2_L__jLLL_.yx/__`\\Wd4C`\ssg/A`\L.aaqzd#RVP`__S$.  `\.yyAqvgqqyg#9fKL@p  Wj$$R$$kLL_  @@$E@6FFso@6@@@@bs.-`----`..__..__   ``                 
   __jdfPP$ELWZTPDUH$EL_ZIZZ9H$LWd$kL_Wd4$kKLQLL_ax--``35tss..```~tY8CL`33~~~A39R8W9+PW91NN$$kWZP5RhmmmFpL..zggwwaxkL__y/ACL....______yXKC..ggyWA4VPP`\L..gg+~____________2$$P7TRbVF _Wj$$R$R$LL____`Gb888@@@@@@W@w@@@@@````o+ouomo---  _.______  _        
 ___j/f$$Z$Dkp#$Lq$N$$LpaqqpZR$EW7A$LWWd3$LLWR6kW``\kW@7PA++qeL__`33Fbug3````7TT~3dTT5W7T5dO#NbLWZID7PRRqggpAiLL@@R\kLW/L__g____.q..q.2Dkxe__3..P2IL__`WWm#F` yxq..wj...aamAAKLDDA\  _WJ$EB$NAAkLL.  `B#8@s8F@--@`@380..~~ooW`Q@`P````` v-------   .       
__.ddf$RRRR$LL2ihdiN#bbKdN$RkUd$WZ5$bLWW4$kLF`\kLL``\gg/```TRXkkqgg__9XWy.`..``S333A\W8dQ7PRR$MhhmmKCLDHAKCLDgjppSZLLgsiL__L..__ggiguyrc@3$kwvrc__`_.. `________ji__jrndVPRDDDkkFP` _Wj$$FEZNNN$kLL.. `.@@@-F```-.-``~~~``````~ .. ``@@``CL````~  `        
wamdf$PPFFRqjppFPPPNj$LLWH4BhWdPhWVA$LWW#$$LL.``gg..-sse- ````\XW4Gu./`jj.psaaaqs/F``599d+P`7TRR9RRhameZ255mK6$DPhhmw#Akugbggpqj.pALVZASyg___ZL_..pgg_______-__u3$kW/CDDPFDW#RC55W  WW4$EEN$ERN$NkLL__ ..``.. ```~ G---.oaoo..``s...-@- Gam--   --     --  
/RRO$DBLL_Z5$ELLLZILd$gLgP5$RI$LDBZR$$LLW3$Lk.ksssLL@38FLggc```33f#MeLuuae@@#RRQQZLWaaW7``5``TTTTT9Wd$$bWWZRLW#AKOIBMKDNVR6K$LNjiF@VKC_gXCL.--waxcL_$LLuaapgqqam####PkWfCDPP__yg~~__Wd$$ENN$ERN$N$kkL_____  L . `` ```~~~sf~~ .@`~~-``` 37R8L  ``` ....``  
FD2Z$$$umpWd4$kkgggggphqLLJlHjmmqgEW#AbWW4$kLLL@#Fkcs@/kWs6F--gg/`33\kW`3$S2P`\34rPW~#QQC`___gg337d9PPR#99Kua.FDaggFF-Wd$NMPAWW4$LWDFkqi$ggggLW3$LLaamWWd6KUUMMPFFFTIIZLFFFLGa8FF  WW4$$ENNRELN#RRN$kLL______       --___````--.` .. -. 4/F        ~~~;    
LqdBRR####N#4RkN##HHBRN4$kRKU2IRN$$W7I$LW3$kkkW.F``@xe.@@38F``WGCL.``\\mmqyp```2ZIL_``3\amwwaaamPA87Z`537PPHtbbWMRELZ2L9PHfKCPH~+F~~NNammKAAkkW_aagdRNNMMRM##fR5CL gaamKFFFWgzFL_  Wd4$FRNNNRKNTNDRRkkkqq._______   ` .....  ``___`. ``.`~ ``__   j.``i.   
Wj$BPRIZZFP2Z55P#ZPBPPU5$KPggggLPAgggp$iW2ARLLLKLL@@8EL.``\..@+Aamsg___~A#xkL__pGae-u-P3##Bd99fP_g7~\WW7F5577PR##9hhmmmBFKZggW``IIZ___ZZlL22$LLWM#RRPP####$TFC5gg_pW2ZPRLLLdSFF__ _Wj$$EEIDDNNELNRR$EV@#amegL________             `.  . ``  _  `  3omaekW` 
Nd$BPR$$$FnqjppWqIgZLLggZFhjZZ$ELPA4VWAhhYFR\bkFL@g@@@ggL_3iL..`3R6mmuuZ``\\wamc@39bV`C2``397``\\aZ``W8``~~~P``57TTT99RRKuammLuaamwuaammmwwwmm##PPP55M6TFP7P~Wd6Gbkgg$FFBmbWPAWWa _W4$$ENEEENN$EPEEPAKW77RNhkpppL______________________      `` _.``~@fF~  
NfBLLN$MlLNqqLLpqqqppLpN$LNqiWRlLLdj$KZDN$L@A\QLk-6@@@A\kW/A\y ___29#+~  ``~~++~--`Q.wweqg2sS..33ssb8g____Z___aaZDWWTT55####$hH#+FP####PRRU7PPTF``_33RR8L``___99#RKGZZDPPFRLLLW~ __jl$ENNNLLWNR$LLKKQDkK``7TNNkkkmeeg______________________  
```

![Mona Lisa](https://github.com/awentzonline/deepascii/raw/master/examples/images/monalisa.jpg)
```
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

