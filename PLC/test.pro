CoDeSys+G                      @        @   2.3.9.48ћ   @   ConfigExtensionу         CommConfigEx7             CommConfigExEnd   ME                  IB                    % QB                    %   ME_End   CMЉ      CM_End   CTХ   џџџџџџџџ   CT_End   ME                 IB                    % QB                    %   ME_End   CM.     CM_End   CTJ  џџџџџџџџ   CT_End   ME                 IB                    % QB                    %   ME_End   CMГ     CM_End   CTЯ  џџџџџџџџ   CT_End   ME$                 IB                    % QB                    %   ME_End   CM8     CM_End   CTT  џџџџџџџџ   CT_End   MEЉ                 IB                    % QB                    %   ME_End   CMН     CM_End   CTй  џџџџџџџџ   CT_End   ConfigExtensionEnd/    @                             ъы` +    @      ЭЭЭЭЭЭЭЭ             њох`        5   @   \   C:\PROGRAM FILES (X86)\WAGO SOFTWARE\CODESYS V2.3\TARGETS\WAGO\LIBRARIES\32_BIT\STANDARD.LIB          ASCIIBYTE_TO_STRING               byt           §џ                 ASCIIBYTE_TO_STRING                                         ќвзL     џџџџ           CONCAT               STR1               §џ              STR2               §џ                 CONCAT                                         ќвзL     џџџџ           CTD           M             §џ           Variable for CD Edge Detection      CD            §џ           Count Down on rising edge    LOAD            §џ	           Load Start Value    PV           §џ
           Start Value       Q            §џ           Counter reached 0    CV           §џ           Current Counter Value             ќвзL     џџџџ           CTU           M             §џ            Variable for CU Edge Detection       CU            §џ       
    Count Up    RESET            §џ	           Reset Counter to 0    PV           §џ
           Counter Limit       Q            §џ           Counter reached the Limit    CV           §џ           Current Counter Value             ќвзL     џџџџ           CTUD           MU             §џ            Variable for CU Edge Detection    MD             §џ            Variable for CD Edge Detection       CU            §џ
       
    Count Up    CD            §џ           Count Down    RESET            §џ           Reset Counter to Null    LOAD            §џ           Load Start Value    PV           §џ           Start Value / Counter Limit       QU            §џ           Counter reached Limit    QD            §џ           Counter reached Null    CV           §џ           Current Counter Value             ќвзL     џџџџ           DELETE               STR               §џ              LEN           §џ	              POS           §џ
                 DELETE                                         ќвзL     џџџџ           F_TRIG           M             §џ                 CLK            §џ           Signal to detect       Q            §џ	           Edge detected             ќвзL     џџџџ           FIND               STR1               §џ	              STR2               §џ
                 FIND                                     ќвзL     џџџџ           INSERT               STR1               §џ	              STR2               §џ
              POS           §џ                 INSERT                                         ќвзL     џџџџ           LEFT               STR               §џ              SIZE           §џ                 LEFT                                         ќвзL     џџџџ           LEN               STR               §џ                 LEN                                     ќвзL     џџџџ           MID               STR               §џ              LEN           §џ	              POS           §џ
                 MID                                         ќвзL     џџџџ           R_TRIG           M             §џ                 CLK            §џ           Signal to detect       Q            §џ	           Edge detected             ќвзL     џџџџ        
   REAL_STATE               RESET            §џ           Reset the variable       ERROR           §џ           Error detected             ќвзL     џџџџ           REPLACE               STR1               §џ	              STR2               §џ
              L           §џ              P           §џ                 REPLACE                                         ќвзL     џџџџ           RIGHT               STR               §џ              SIZE           §џ                 RIGHT                                         ќвзL     џџџџ           RS               SET            §џ              RESET1            §џ	                 Q1            §џ                       ќвзL     џџџџ           RTC           M             §џ              DiffTime            §џ                 EN            §џ              PDT           §џ                 Q            §џ              CDT           §џ                       ќвзL     џџџџ           SEMA           X             §џ                 CLAIM            §џ
              RELEASE            §џ                 BUSY            §џ                       ќвзL     џџџџ           SR               SET1            §џ              RESET            §џ                 Q1            §џ                       ќвзL     џџџџ           STANDARD_VERSION               EN            §џ                 STANDARD_VERSION                                     ќвзL     џџџџ           STRING_COMPARE               STR1               §џ              STR2               §џ                 STRING_COMPARE                                      ќвзL     џџџџ           STRING_TO_ASCIIBYTE               str               §џ                 STRING_TO_ASCIIBYTE                                     ќвзL     џџџџ           TOF           M             §џ           internal variable 	   StartTime            §џ           internal variable       IN            §џ       ?    starts timer with falling edge, resets timer with rising edge    PT           §џ           time to pass, before Q is set       Q            §џ       2    is FALSE, PT seconds after IN had a falling edge    ET           §џ           elapsed time             ќвзL     џџџџ           TON           M             §џ           internal variable 	   StartTime            §џ           internal variable       IN            §џ       ?    starts timer with rising edge, resets timer with falling edge    PT           §џ           time to pass, before Q is set       Q            §џ       0    is TRUE, PT seconds after IN had a rising edge    ET           §џ           elapsed time             ќвзL     џџџџ           TP        	   StartTime            §џ           internal variable       IN            §џ       !    Trigger for Start of the Signal    PT           §џ       '    The length of the High-Signal in 10ms       Q            §џ           The pulse    ET           §џ       &    The current phase of the High-Signal             ќвзL     џџџџ    b   C:\PROGRAM FILES (X86)\WAGO SOFTWARE\CODESYS V2.3\TARGETS\WAGO\LIBRARIES\32_BIT\SYSLIBCALLBACK.LIB          SYSCALLBACKREGISTER            	   iPOUIndex           §џ       !    POU Index of callback function.    Event            	   RTS_EVENT   §џ           Event to register       SysCallbackRegister                                      ќвзL     џџџџ           SYSCALLBACKUNREGISTER            	   iPOUIndex           §џ       !    POU Index of callback function.    Event            	   RTS_EVENT   §џ           Event to register       SysCallbackUnregister                                      ќвзL     џџџџ    [   C:\PROGRAM FILES (X86)\WAGO SOFTWARE\CODESYS V2.3\TARGETS\WAGO\LIBRARIES\32_BIT\SERCOMM.LIB          SERCOMM           INTERNAL_USE_DO_NOT_MODIFY   	                         §џ                 EN            §џ           Initial = FALSE    COMPORT           §џ           Initial = COM1    BAUDRATE               COM_BAUDRATE   §џ           Initial = 19200 Baud    PARITY            
   COM_PARITY   §џ           Initial = even parity    STOPBITS               COM_STOPBITS   §џ	           Initial = one stopbit    BYTESIZE               COM_BYTESIZE   §џ
           Initial = 8 Databits    FLOW_CONTROL               COM_FLOW_CONTROL   §џ           Initial = No flow control 	   FB_ACTION            
   COM_ACTION   §џ           Initial = Open    BYTES_TO_DO           §џ           Initial = 0    SEND_BUFFER           §џ           Address of the send buffer    RECEIVE_BUFFER           §џ           Address of the receive buffer       ENO            §џ              ERROR            §џ           Indicates an error 
   LAST_ERROR           §џ           Error code 
   BYTES_DONE           §џ           Number of write/read bytes             xфM     џџџџ           SERCOMM_VERSION               EN            §џ          Activate the function       SERCOMM_VERSION                                     xфM     џџџџ    l   C:\PROGRAM FILES (X86)\WAGO SOFTWARE\CODESYS V2.3\TARGETS\WAGO\LIBRARIES\APPLICATION\SERIAL_INTERFACE_01.LIB          SERIAL_COM_OBJECT           COM                                     SERIAL_INTERFACE    §џ              INIT             §џ                 OPEN_COM_PORT           §џ              COM_PORT_NR          §џ              BAUDRATE       
    BAUD_9600       COM_BAUDRATE   §џ              PARITY       
    PARITY_NO    
   COM_PARITY   §џ              STOPBITS           STOPBITS_1       COM_STOPBITS   §џ              BYTESIZE           BS_8        COM_BYTESIZE   §џ              FLOW_CONTROL           FLOW_CONTROL_TERMINAL_DEFAULT        COM_FLOW_CONTROL   §џ           	   Interface                     I_SERIAL_COM   §џ                           жuQ      џџџџ           SERIAL_INTERFACE     	   	   Interface                              SERCOMM    §џ,              Com_Port_Ist_Offen             §џ.              Senden_Ist_Aktiv             §џ/              Fehler            §џ0              Buffer   	                         §џ2              i            §џ3              Receive_aktiv             §џ4              Byte_to_read            §џ5              step            §џ7           	      xOPEN_COM_PORT            §џ              bCOM_PORT_NR           §џ           
   cbBAUDRATE           BAUDRATE_TERMINAL_DEFAULT       COM_BAUDRATE   §џ              cpPARITY           PARITY_TERMINAL_DEFAULT    
   COM_PARITY   §џ           
   csSTOPBITS           STOPBITS_TERMINAL_DEFAULT       COM_STOPBITS   §џ              cbsBYTESIZE           BYTESIZE_TERMINAL_DEFAULT        COM_BYTESIZE   §џ              cfFLOW_CONTROL           FLOW_CONTROL_TERMINAL_DEFAULT        COM_FLOW_CONTROL   §џ              iBYTES_TO_SEND           §џ              ptSEND_BUFFER                 §џ                  bERROR           §џ(              xCOM_PORT_IS_OPEN            §џ)                 xSTART_SEND            §џ#              utRECEIVE_BUFFER                 typRING_BUFFER  §џ$              xINIT            §џ%                   жuQ      џџџџ           VERSION_SERIALINTERFACE           _VERSION         §џ           Version 2.6   |  28.11.2012       EN            §џ                 Version_SerialInterface                                     жuQ      џџџџ                  COM3        
   PT_SendStr    	  џ                             F            	   PT_TmpStr    	  џ                             F            
   SendString    Q      070Q     F            	   M_RECVSTR             F            	   M_SENDSTR            F        -    Communicationparams FOR 750-65x/003-000 only	   wBaudRate          F 	           	   bDataBits           F 
              bParity            F           0=NO   bFlowControl           F        
   1=XON/XOFF   i            F               in_COM_Port           F        
   COM ******   COM                                     SERIAL_INTERFACE    F            	   xOpenPort            F            	   xInitPort             F               xSendActive             F               ReceiveBuffer                typRing_Buffer    F               ReceiveBufferOldIndex            F               ReceiveString                F               pReceiveStr    	  џ                             F               bERROR            F            
   Messwert01             F                                Ьщы`  @    џџџџ           PLC_PRG        
   PT_SendStr    	  џ                             .            	   PT_TmpStr    	  џ                             .            
   SendString    Q      070Q     .            	   M_RECVSTR             .            	   M_SENDSTR            .        -    Communicationparams FOR 750-65x/003-000 only	   wBaudRate          . 	           	   bDataBits           . 
              bParity            .           0=NO   bFlowControl           .        
   1=XON/XOFF   i            .               in_COM_Port           .        
   COM ******   COM                                     SERIAL_INTERFACE    .            	   xOpenPort            .            	   xInitPort             .               xSendActive             .               ReceiveBuffer                typRing_Buffer    .               ReceiveBufferOldIndex            .               ReceiveString                .               pReceiveStr    	  џ                             .               bERROR            .            
   Messwert01             .                                Wтх`  @    џџџџ            
 э   .      F   ( t9      K   9     K   9     K   9     K   Г9                 Р9         +           %  %      AUX)K^дО PWWВ            Ethernet (TCP/IP)  Local_ WAGO Ethernet TCP/IP driver    <   ш  IP address target node IP address 
   192.168.1.129 <   щ  port number target node port number    	      џџ  O   ъ  transport protocol transport protocol used               tcp    udp 9               AБ№њгЌH ZJВ            Tcp/Ip (Level 2 Route)  192_168_1_128 3S Tcp/Ip Level 2 Router Driver    9   щ  Address IP address or hostname 
   192.168.1.129    ш  Port     	   ќ  TargetId         7   d   Motorola byteorder                No    Yes %      AUX)K^дО PWWВ            Ethernet (TCP/IP)  Local_ WAGO Ethernet TCP/IP driver    <   ш  IP address target node IP address 
   192.168.1.129 <   щ  port number target node port number    	      џџ  O   ъ  transport protocol transport protocol used               tcp    udp   K         @   њох``        ЭЭЭЭЭЭЭЭ                     CoDeSys 1-2.2   рџџџ  ЭЭЭЭЭЭЭЭ                     в.  u       ы      
   ђ         ѓ         ї          ј                    "          $                                                   '          (          Б          Г          Е          Й          К         Ж          Я          а          б         М          О          Р          Т          Ф         Ц         Ъ       P  Ш          Ь         Ю         в                    ~                                                                                                                                                                                 @         @         @         @         @         @  Ђ                   Ј                   M         N          O          P          `         a          t          y          z          b         c          X          d         e         _          Q          \         R          K          U         X         Z         т          ф         ц      
   ш         ъ         ь         ю         ё         я          №          ђ         ѓ      џџџџє          ѕ          ї      (                                                                        "         !          #          $                   ^          f         g          h          i          j          k         F          H         J         L          N         P         R          U         S          T          V          W          Є          Ѕ          l          o          p          q          r          s         u          о          v         І          Ї      џџџџ|         ~                  x          z      (   Љ          Ћ         %         ­          Ў          Џ         @         н          ф          и         &          №          	                   ц          ч          ш         щ          ъ         Њ          В          Д          Ќ          ­          Џ          А          З          И          О          ь          э                            I         J         K          	          L         M                                       о          P         Q          S          )          	          	                     	          +	       @  ,	       @  -	      џџџџZ	      џџџџЭЭЭЭ        џџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџв.  ђ         ѓ         ї          ј                    "          $                                                   '          (          Б          Г          Е          Й          К         Ж          Я          а          б         М          О          Р          Т          Ф         Ц         Ъ       P  Ш          Ь         Ю         в                 @         а        @         @  Ђ      џ  Ј         a          t          y          z          b          c          X          d         e         _         \         R          K          U        UDPX         Z         т          ф         ц      
   ш         ъ         ь         ю         ё         я          №          ђ         ѓ      џџџџє          ѕ          ї      (   "          #         $                    g          h          i          j          k         F          H         J         L          N         P         R          U         S          T          V          W          Є          o          p          q          r          s          u          о          v         w          Ї         |         ~                  x          z      (   Љ          %         ­          Ў          Џ         @         н          р         с      X  ф          и         &         с№          	                   ц          ч          ш         щ          ъ         Њ          В          Д          Ќ          ­          Џ          А          З          И          О          ы          ь         э          ў          џ                                       I         J         K          	          L         M                                       о          P         Q          S          )          	          	                     	          +	       @  ,	       @  -	      џџџџZ	      џџџџЭЭЭЭ        џџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџЭЭЭЭљџџџ  ЭЭЭЭЭЭЭЭ                                                   Ї  	   	   Name                 џџџџ
   Index                 џџ         SubIndex                 џ          Accesslevel          !         low   middle   high       Accessright          1      	   read only
   write only
   read-write       Variable    	             џџџџ
   Value                Variable       Min                Variable       Max                Variable          5  
   	   Name                 џџџџ
   Index                 џџ         SubIndex                 џ          Accesslevel          !         low   middle   high       Accessright          1      	   read only
   write only
   read-write    	   Type          ~         INT   UINT   DINT   UDINT   LINT   ULINT   SINT   USINT   BYTE   WORD   DWORD   REAL   LREAL   STRING    
   Value                Type       Default                Type       Min                Type       Max                Type          5  
   	   Name                 џџџџ
   Index                 џџ         SubIndex                 џ          Accesslevel          !         low   middle   high       Accessright          1      	   read only
   write only
   read-write    	   Type          ~         INT   UINT   DINT   UDINT   LINT   ULINT   SINT   USINT   BYTE   WORD   DWORD   REAL   LREAL   STRING    
   Value                Type       Default                Type       Min                Type       Max                Type          d        Member    	             џџџџ   Index-Offset                 џџ         SubIndex-Offset                 џ          Accesslevel          !         low   middle   high       Accessright          1      	   read only
   write only
   read-write       Min                Member       Max                Member            	   	   Name                 џџџџ   Member    	             џџџџ
   Value                Member    
   Index                 џџ         SubIndex                 џ          Accesslevel          !         low   middle   high       Accessright          1      	   read only
   write only
   read-write       Min                Member       Max                Member          Ї  	   	   Name                 џџџџ
   Index                 џџ         SubIndex                 џ          Accesslevel          !         low   middle   high       Accessright          1      	   read only
   write only
   read-write       Variable    	             џџџџ
   Value                Variable       Min                Variable       Max                Variable                         ђџџџ  ЭЭЭЭЭЭЭЭ                  _Dummy@    @   @@    @   @             Єя@             Єя@@   @     v@@   ; @+   ёџџџ  ЭЭЭЭЭЭЭЭ                                  v@      4@   А             v@      D@   А                       Р       @                           f@      4@     f@                v@     f@     @u@     f@        їСы             Module.Root-1__not_found__    Hardware configurationџџџџ IB          % QB          % MB          %   o     Module.K_Bus1Module.Root    K-Bus     IB          % QB          % MB          %    o     Module.FB_VARS2Module.Root    Fieldbus variables    IB          % QB          % MB          %    o     Module.FLAG_VARS3Module.Root    Flag variables    IB          % QB          % MB          %    o     Module.MB_MASTER4Module.Root    Modbus-Master    IB          % QB          % MB          %    њох`	)пх`     ЭЭЭЭЭЭЭЭ           VAR_GLOBAL
END_VAR
                                                                                  "   , 2 2 ѓЕ             Serial3Ш        COM3();џџџџ               ъы`                   start   Called when program starts    _   FUNCTION systemevent: DWORD VAR_INPUT dwEvent: DWORD; dwFilter: DWORD; dwOwner: DWORD; END_VAR     в.     stop   Called when program stops    _   FUNCTION systemevent: DWORD VAR_INPUT dwEvent: DWORD; dwFilter: DWORD; dwOwner: DWORD; END_VAR     в.     before_reset   Called before reset takes place    _   FUNCTION systemevent: DWORD VAR_INPUT dwEvent: DWORD; dwFilter: DWORD; dwOwner: DWORD; END_VAR     в.     after_reset   Called after reset took place    _   FUNCTION systemevent: DWORD VAR_INPUT dwEvent: DWORD; dwFilter: DWORD; dwOwner: DWORD; END_VAR     в.     shutdownC   Called before shutdown is performed (Firmware update over ethernet)    _   FUNCTION systemevent: DWORD VAR_INPUT dwEvent: DWORD; dwFilter: DWORD; dwOwner: DWORD; END_VAR     в.     excpt_watchdog%   Software watchdog of IEC-task expired    _   FUNCTION systemevent: DWORD VAR_INPUT dwEvent: DWORD; dwFilter: DWORD; dwOwner: DWORD; END_VAR     в.     excpt_fieldbus   Fieldbus error    _   FUNCTION systemevent: DWORD VAR_INPUT dwEvent: DWORD; dwFilter: DWORD; dwOwner: DWORD; END_VAR  	   в.     excpt_ioupdate
   KBus error    _   FUNCTION systemevent: DWORD VAR_INPUT dwEvent: DWORD; dwFilter: DWORD; dwOwner: DWORD; END_VAR  
   в.     excpt_dividebyzero*   Division by zero. Only integer operations!    _   FUNCTION systemevent: DWORD VAR_INPUT dwEvent: DWORD; dwFilter: DWORD; dwOwner: DWORD; END_VAR     в.     excpt_noncontinuable   Exception handler    _   FUNCTION systemevent: DWORD VAR_INPUT dwEvent: DWORD; dwFilter: DWORD; dwOwner: DWORD; END_VAR     в.     after_reading_inputs   Called after reading of inputs    _   FUNCTION systemevent: DWORD VAR_INPUT dwEvent: DWORD; dwFilter: DWORD; dwOwner: DWORD; END_VAR     в.     before_writing_outputs    Called before writing of outputs    _   FUNCTION systemevent: DWORD VAR_INPUT dwEvent: DWORD; dwFilter: DWORD; dwOwner: DWORD; END_VAR     в.  
   debug_loop   Debug loop at breakpoint    _   FUNCTION systemevent: DWORD VAR_INPUT dwEvent: DWORD; dwFilter: DWORD; dwOwner: DWORD; END_VAR     в.     online_change+   Is called after CodeInit() at Online-Change    _   FUNCTION systemevent: DWORD VAR_INPUT dwEvent: DWORD; dwFilter: DWORD; dwOwner: DWORD; END_VAR  !   в.     before_download$   Is called before the Download starts    _   FUNCTION systemevent: DWORD VAR_INPUT dwEvent: DWORD; dwFilter: DWORD; dwOwner: DWORD; END_VAR  "   в.     event_login/   Is called before the login service is performed    _   FUNCTION systemevent: DWORD VAR_INPUT dwEvent: DWORD; dwFilter: DWORD; dwOwner: DWORD; END_VAR  ѕ  в.     eth_overload   Ethernet Overload    _   FUNCTION systemevent: DWORD VAR_INPUT dwEvent: DWORD; dwFilter: DWORD; dwOwner: DWORD; END_VAR  ю  в.     eth_network_ready@   Is called directly after the Network and the PLC are initialised    _   FUNCTION systemevent: DWORD VAR_INPUT dwEvent: DWORD; dwFilter: DWORD; dwOwner: DWORD; END_VAR  я  в.  
   blink_codeN   New blink code / Blink code cleared ( Call STATUS_GET_LAST_ERROR for details )    _   FUNCTION systemevent: DWORD VAR_INPUT dwEvent: DWORD; dwFilter: DWORD; dwOwner: DWORD; END_VAR  №  в.     interrupt_0(   Interrupt Real Time Clock (every second)    _   FUNCTION systemevent: DWORD VAR_INPUT dwEvent: DWORD; dwFilter: DWORD; dwOwner: DWORD; END_VAR  ш  в.  $ћџџџ  ЭЭЭЭЭЭЭЭ               ЭЭЭЭЭЭЭЭ           Standard њох`	њох`      ЭЭЭЭЭЭЭЭ                         	пх`     ЭЭЭЭЭЭЭЭ           VAR_CONFIG
END_VAR
                                                                                   '                ЭЭЭЭЭЭЭЭ           Global_Variables ќох`	ќох`     ЭЭЭЭЭЭЭЭ           VAR_GLOBAL
END_VAR
                                                                                               '           	     ЭЭЭЭЭЭЭЭ           Variable_Configuration ќох`	ќох`	     ЭЭЭЭЭЭЭЭ           VAR_CONFIG
END_VAR
                                                                                                    |0|0 @v    @T   Courier @       HH':'mm':'ss @      dd'-'MM'-'yyyy   dd'-'MM'-'yyyy HH':'mm':'ss                                  .     џ   џџџ  Ь3 џџџ   џ џџџ     
    @џ  џџџ     @      DEFAULT             System         |0|0 @v    @T   Courier @       HH':'mm':'ss @      dd'-'MM'-'yyyy   dd'-'MM'-'yyyy HH':'mm':'ss                         )   HH':'mm':'ss @                             dd'-'MM'-'yyyy @       '     F   ,   к           COM3 ощы`	Ьщы`      ЭЭЭЭЭЭЭЭ        и  PROGRAM COM3
VAR
	PT_SendStr : POINTER TO ARRAY[0..255] OF BYTE;
	PT_TmpStr : POINTER TO ARRAY[0..255] OF BYTE;
	SendString : STRING:='070';
	M_RECVSTR : BOOL:=FALSE;
	M_SENDSTR : BOOL:=TRUE;
(* Communicationparams FOR 750-65x/003-000 only*)
	wBaudRate : WORD := 5760;
	bDataBits : BYTE := 8;
	bParity : BYTE := 0; (*0=NO*)
	bFlowControl : BYTE := 4; (*1=XON/XOFF*)
	i : INT;
	in_COM_Port : INT := INT#3;
(*COM *******)
	COM : SERIAL_INTERFACE;
	xOpenPort : BOOL := TRUE;
	xInitPort : BOOL;
	xSendActive : BOOL;
	ReceiveBuffer: typRing_Buffer;
	ReceiveBufferOldIndex : INT;
	ReceiveString : STRING(255);
	pReceiveStr : POINTER TO ARRAY[0..255] OF BYTE;
	bERROR : BYTE :=16#00;
	Messwert01: REAL;
END_VARк  COM( bCOM_PORT_NR := INT_TO_BYTE(in_COM_Port),
  cbBAUDRATE        := wBaudRate,
  cbsBYTESIZE       := bDataBits,
  cpPARITY          := bParity,
  csSTOPBITS        := STOPBITS_1,
  cfFLOW_CONTROL    := bFlowControl,
  utRECEIVE_BUFFER  := ReceiveBuffer,
  ptSEND_BUFFER     := ADR(SendString),
  xINIT             := xInitPort,
  xOPEN_COM_PORT    := xOpenPort,
  iBYTES_TO_SEND    := LEN(SendString)+1,
  xSTART_SEND       := M_SENDSTR);
bERROR:=COM.bERROR;

IF pReceiveStr = 0 THEN (*Empfangspuffer mit Adresse von Empfangsstring initialisieren*)

  pReceiveStr := ADR( ReceiveString );

END_IF;

IF ReceiveBuffer.Index>0 THEN (*Neue Daten empfangen*)

IF ReceiveBuffer.Data[ ReceiveBuffer.Index-1 ] = 16#0A THEN (*16#0A=LF(Linefeed)*)

     FOR i:=0 TO 255 DO

        pReceiveStr^[i]:=16#00;  (*Empfangspuffer lіschen*)

     END_FOR;

     FOR i:=0 TO ReceiveBuffer.Index-1 DO

        pReceiveStr^[i] :=  ReceiveBuffer.Data[ i ]; (*Ringpufferdaten in Empfangspuffer kopieren*)

     END_FOR;

     M_RECVSTR:=TRUE;

     ReceiveBuffer.Index:=0; (*Index des Ringpuffers zurќcksetzen*)

END_IF;

END_IF;

(*Messwert01 := (WORD_TO_REAL(WPACK(ReceiveBuffer.Data[0], ReceiveBuffer.Data[1])));*)               .   ,   Юђ           PLC_PRG Wтх`	Wтх`      ЭЭЭЭЭЭЭЭ        л  PROGRAM PLC_PRG
VAR
	PT_SendStr : POINTER TO ARRAY[0..255] OF BYTE;
	PT_TmpStr : POINTER TO ARRAY[0..255] OF BYTE;
	SendString : STRING:='070';
	M_RECVSTR : BOOL:=FALSE;
	M_SENDSTR : BOOL:=TRUE;
(* Communicationparams FOR 750-65x/003-000 only*)
	wBaudRate : WORD := 5760;
	bDataBits : BYTE := 8;
	bParity : BYTE := 0; (*0=NO*)
	bFlowControl : BYTE := 4; (*1=XON/XOFF*)
	i : INT;
	in_COM_Port : INT := INT#2;
(*COM *******)
	COM : SERIAL_INTERFACE;
	xOpenPort : BOOL := TRUE;
	xInitPort : BOOL;
	xSendActive : BOOL;
	ReceiveBuffer: typRing_Buffer;
	ReceiveBufferOldIndex : INT;
	ReceiveString : STRING(255);
	pReceiveStr : POINTER TO ARRAY[0..255] OF BYTE;
	bERROR : BYTE :=16#00;
	Messwert01: REAL;
END_VARк  COM( bCOM_PORT_NR := INT_TO_BYTE(in_COM_Port),
  cbBAUDRATE        := wBaudRate,
  cbsBYTESIZE       := bDataBits,
  cpPARITY          := bParity,
  csSTOPBITS        := STOPBITS_1,
  cfFLOW_CONTROL    := bFlowControl,
  utRECEIVE_BUFFER  := ReceiveBuffer,
  ptSEND_BUFFER     := ADR(SendString),
  xINIT             := xInitPort,
  xOPEN_COM_PORT    := xOpenPort,
  iBYTES_TO_SEND    := LEN(SendString)+1,
  xSTART_SEND       := M_SENDSTR);
bERROR:=COM.bERROR;

IF pReceiveStr = 0 THEN (*Empfangspuffer mit Adresse von Empfangsstring initialisieren*)

  pReceiveStr := ADR( ReceiveString );

END_IF;

IF ReceiveBuffer.Index>0 THEN (*Neue Daten empfangen*)

IF ReceiveBuffer.Data[ ReceiveBuffer.Index-1 ] = 16#0A THEN (*16#0A=LF(Linefeed)*)

     FOR i:=0 TO 255 DO

        pReceiveStr^[i]:=16#00;  (*Empfangspuffer lіschen*)

     END_FOR;

     FOR i:=0 TO ReceiveBuffer.Index-1 DO

        pReceiveStr^[i] :=  ReceiveBuffer.Data[ i ]; (*Ringpufferdaten in Empfangspuffer kopieren*)

     END_FOR;

     M_RECVSTR:=TRUE;

     ReceiveBuffer.Index:=0; (*Index des Ringpuffers zurќcksetzen*)

END_IF;

END_IF;

(*Messwert01 := (WORD_TO_REAL(WPACK(ReceiveBuffer.Data[0], ReceiveBuffer.Data[1])));*)                 §џџџ, 2 2 ч         #   Standard.lib 8.11.10 12:37:48 @ќвзL)   SYSLIBCALLBACK.LIB 8.11.10 12:37:48 @ќвзL"   SerComm.lib 31.5.11 09:06:48 @фM.   Serial_Interface_01.lib 22.4.13 12:50:14 @цuQ   !   ASCIIBYTE_TO_STRING @                  CONCAT @        	   CTD @        	   CTU @        
   CTUD @           DELETE @           F_TRIG @        
   FIND @           INSERT @        
   LEFT @        	   LEN @        	   MID @           R_TRIG @           REAL_STATE @          REPLACE @           RIGHT @           RS @        	   RTC @        
   SEMA @           SR @           STANDARD_VERSION @          STRING_COMPARE @          STRING_TO_ASCIIBYTE @       	   TOF @        	   TON @           TP @              Global Variables 0 @           b   SysCallbackRegister @   	   RTS_EVENT       RTS_EVENT_FILTER       RTS_EVENT_SOURCE                   SysCallbackUnregister @              Globale_Variablen @           Version @              SERCOMM @   
   COM_ACTION       COM_BAUDRATE       COM_BYTESIZE       COM_FLOW_CONTROL    
   COM_PARITY       COM_STOPBITS                   SERCOMM_VERSION @              Globale_Variablen @           I   SERIAL_COM_OBJECT @      I_SERIAL_COM       typRING_BUFFER                  SERIAL_INTERFACE @       !   SERIAL_INTERFACE.CLOSE_PORT @           SERIAL_INTERFACE.OPEN_PORT @       #   SERIAL_INTERFACE.RECEIVE_DATA @           SERIAL_INTERFACE.SEND_DATA @          Version_SerialInterface @             Globale_InterfaceConstant @                          ЭЭЭЭЭЭЭЭ           2 ѓ  ѓ           џџџџџџџџџџџџџџџџ  
             њџџџ  ЭЭЭЭЭЭЭЭ        јџџџ  ЭЭЭЭЭЭЭЭ                      POUs                COM3  F                   PLC_PRG  .   џџџџ          
   Data types  џџџџ             Visualizations  џџџџ               Global Variables                 Global_Variables                     Variable_Configuration  	   џџџџ                                         ЭЭЭЭЭЭЭЭ             ќох`в.             в.                	   localhost            P      	   localhost            P      	   localhost            P     пх` ь§N