CoDeSys+Є                     @        @   2.3.9.48ч    @   ConfigExtensionЯ          CommConfigEx7             CommConfigExEnd   ME                  IB    ќ"  Ь!  r,  as  % QB    X^  `!     @   %   ME_End   CMЉ      CM_End   CTХ   џџџџџџџџ   CT_End   ConfigExtensionEnd/    @                             oЧX_ +    @      ЭЭЭЭЭЭЭЭ             ­1B        ТR   @   Q   C:\Program Files (x86)\Common Files\CAA-Targets\3S\Lib_PLCWinNT\SysLibSockets.lib          SYSSOCKACCEPT               diSocket           §џ           	   pSockAddr           §џ       (    Address of SocketAddress (SOCKADDRESS)    piSockAddrSize           §џ       &    Address of socket address size (DINT)      SysSockAccept                                     ЦX_     џџџџ           SYSSOCKBIND               diSocket           §џ           	   pSockAddr           §џ       (    Address of SocketAddress (SOCKADDRESS)    diSockAddrSize           §џ           Size of socket address       SysSockBind                                      ЦX_     џџџџ           SYSSOCKCLOSE               diSocket           §џ                 SysSockClose                                      ЦX_     џџџџ           SYSSOCKCONNECT               diSocket           §џ           	   pSockAddr           §џ       (    Address of SocketAddress (SOCKADDRESS)    diSockAddrSize           §џ           Size of socket address       SysSockConnect                                      ЦX_     џџџџ           SYSSOCKCREATE               diAddressFamily           §џ              diType           §џ           
   diProtocol           §џ                 SysSockCreate                                     ЦX_     џџџџ           SYSSOCKGETHOSTBYNAME            
   stHostName     Q       Q         §џ                 SysSockGetHostByName                                     ЦX_     џџџџ           SYSSOCKGETHOSTNAME            
   stHostName     Q       Q         §џ              diNameLength           §џ                 SysSockGetHostName                                      ЦX_     џџџџ           SYSSOCKGETLASTERROR        
   adwJobData   	                          §џ           
   bOldEnable             §џ                 bEnable            §џ              diSocket           §џ                 bDone            §џ              bBusy            §џ              bError            §џ	              wErrorId           §џ
              dwLastError           §џ                       ЦX_     џџџџ           SYSSOCKGETLASTERRORSYNC               diSocket           §џ                 SysSockGetLastErrorSync                                     ЦX_     џџџџ           SYSSOCKGETOPTION               diSocket           §џ              diLevel           §џ              diOption           §џ              pOptionValue           §џ           Address of option    piOptionLength           §џ           Address of option size (DINT)       SysSockGetOption                                      ЦX_     џџџџ           SYSSOCKHTONL               dwHost           §џ                 SysSockHtonl                                     ЦX_     џџџџ           SYSSOCKHTONS               wHost           §џ                 SysSockHtons                                     ЦX_     џџџџ           SYSSOCKINETADDR               stIPAddr    Q       Q    §џ                 SysSockInetAddr                                     ЦX_     џџџџ           SYSSOCKINETNTOA               InAddr               INADDR   §џ              stIPAddr    Q       Q    §џ              diIPAddrSize           §џ                 SysSockInetNtoa                                      ЦX_     џџџџ           SYSSOCKIOCTL               diSocket           §џ           	   diCommand           §џ              piParameter           §џ           Address of parameter (DINT)       SysSockIoctl                                     ЦX_     џџџџ           SYSSOCKLISTEN               diSocket           §џ              diMaxConnections           §џ                 SysSockListen                                      ЦX_     џџџџ           SYSSOCKNTOHL               dwNet           §џ                 SysSockNtohl                                     ЦX_     џџџџ           SYSSOCKNTOHS               wNet           §џ                 SysSockNtohs                                     ЦX_     џџџџ           SYSSOCKRECV               diSocket           §џ           	   pbyBuffer           §џ           Address of buffer to receive    diBufferSize           §џ              diFlags           §џ                 SysSockRecv                                     ЦX_     џџџџ           SYSSOCKRECVFROM               diSocket           §џ           	   pbyBuffer           §џ           Address of buffer to receive    diBufferSize           §џ              diFlags           §џ           	   pSockAddr           §џ       &    Address of socket address SOCKADDRESS   diSockAddrSize           §џ           Size of socket address       SysSockRecvFrom                                     ЦX_     џџџџ           SYSSOCKSELECT               diWidth           §џ           Typically SOCKET_FD_SETSIZE    fdRead           §џ           Address of  SOCKET_FD_SET    fdWrite           §џ           Address of  SOCKET_FD_SET    fdExcept           §џ           Address of  SOCKET_FD_SET 
   ptvTimeout           §џ           Address of SOCKET_TIMEVAL       SysSockSelect                                     ЦX_     џџџџ           SYSSOCKSEND               diSocket           §џ           	   pbyBuffer           §џ           Address of buffer to receive    diBufferSize           §џ              diFlags           §џ                 SysSockSend                                     ЦX_     џџџџ           SYSSOCKSENDTO               diSocket           §џ           	   pbyBuffer           §џ           Address of buffer to receive    diBufferSize           §џ              diFlags           §џ           	   pSockAddr           §џ       '    Address of socket address SOCKADDRESS    diSockAddrSize           §џ           Size of socket address       SysSockSendTo                                     ЦX_     џџџџ           SYSSOCKSETIPADDRESS            
   stCardName    Q       Q    §џ              stIPAddress    Q       Q    §џ                 SysSockSetIPAddress                                      ЦX_     џџџџ           SYSSOCKSETOPTION               diSocket           §џ              diLevel           §џ              diOption           §џ              pOptionValue           §џ           Address of option    diOptionLength           §џ           Length of option       SysSockSetOption                                      ЦX_     џџџџ           SYSSOCKSHUTDOWN               diSocket           §џ              diHow           §џ                 SysSockShutdown                                      ЦX_     џџџџ    F   C:\Program Files (x86)\WAGO Software\CODESYS V2.3\Library\Standard.lib          CONCAT               STR1               §џ              STR2               §џ                 CONCAT                                         ЦX_     џџџџ           CTD           M             §џ           Variable for CD Edge Detection      CD            §џ           Count Down on rising edge    LOAD            §џ	           Load Start Value    PV           §џ
           Start Value       Q            §џ           Counter reached 0    CV           §џ           Current Counter Value             ЦX_     џџџџ           CTU           M             §џ            Variable for CU Edge Detection       CU            §џ       
    Count Up    RESET            §џ	           Reset Counter to 0    PV           §џ
           Counter Limit       Q            §џ           Counter reached the Limit    CV           §џ           Current Counter Value             ЦX_     џџџџ           CTUD           MU             §џ            Variable for CU Edge Detection    MD             §џ            Variable for CD Edge Detection       CU            §џ
       
    Count Up    CD            §џ           Count Down    RESET            §џ           Reset Counter to Null    LOAD            §џ           Load Start Value    PV           §џ           Start Value / Counter Limit       QU            §џ           Counter reached Limit    QD            §џ           Counter reached Null    CV           §џ           Current Counter Value             ЦX_     џџџџ           DELETE               STR               §џ              LEN           §џ	              POS           §џ
                 DELETE                                         ЦX_     џџџџ           F_TRIG           M             §џ                 CLK            §џ           Signal to detect       Q            §џ	           Edge detected             ЦX_     џџџџ           FIND               STR1               §џ	              STR2               §џ
                 FIND                                     ЦX_     џџџџ           INSERT               STR1               §џ	              STR2               §џ
              POS           §џ                 INSERT                                         ЦX_     џџџџ           LEFT               STR               §џ              SIZE           §џ                 LEFT                                         ЦX_     џџџџ           LEN               STR               §џ                 LEN                                     ЦX_     џџџџ           MID               STR               §џ              LEN           §џ	              POS           §џ
                 MID                                         ЦX_     џџџџ           R_TRIG           M             §џ                 CLK            §џ           Signal to detect       Q            §џ	           Edge detected             ЦX_     џџџџ           REPLACE               STR1               §џ	              STR2               §џ
              L           §џ              P           §џ                 REPLACE                                         ЦX_     џџџџ           RIGHT               STR               §џ              SIZE           §џ                 RIGHT                                         ЦX_     џџџџ           RS               SET            §џ              RESET1            §џ	                 Q1            §џ                       ЦX_     џџџџ           RTC           M             §џ              DiffTime            §џ                 EN            §џ              PDT           §џ                 Q            §џ              CDT           §џ                       ЦX_     џџџџ           SEMA           X             §џ                 CLAIM            §џ
              RELEASE            §џ                 BUSY            §џ                       ЦX_     џџџџ           SR               SET1            §џ              RESET            §џ                 Q1            §џ                       ЦX_     џџџџ           TOF           M             §џ           internal variable 	   StartTime            §џ           internal variable       IN            §џ       ?    starts timer with falling edge, resets timer with rising edge    PT           §џ           time to pass, before Q is set       Q            §џ       2    is FALSE, PT seconds after IN had a falling edge    ET           §џ           elapsed time             ЦX_     џџџџ           TON           M             §џ           internal variable 	   StartTime            §џ           internal variable       IN            §џ       ?    starts timer with rising edge, resets timer with falling edge    PT           §џ           time to pass, before Q is set       Q            §џ       0    is TRUE, PT seconds after IN had a rising edge    ET           §џ           elapsed time             ЦX_     џџџџ           TP        	   StartTime            §џ           internal variable       IN            §џ       !    Trigger for Start of the Signal    PT           §џ       '    The length of the High-Signal in 10ms       Q            §џ           The pulse    ET           §џ       &    The current phase of the High-Signal             ЦX_     џџџџ    R   C:\Program Files (x86)\Common Files\CAA-Targets\3S\Lib_PLCWinNT\SYSLIBCALLBACK.LIB          SYSCALLBACKREGISTER            	   iPOUIndex           §џ       !    POU Index of callback function.    Event            	   RTS_EVENT   §џ           Event to register       SysCallbackRegister                                      ЦX_     џџџџ           SYSCALLBACKUNREGISTER            	   iPOUIndex           §џ       !    POU Index of callback function.    Event            	   RTS_EVENT   §џ           Event to register       SysCallbackUnregister                                      ЦX_     џџџџ                  CONVERTPADDRESSTOSTRING           iadr               INADDR    P 	              stIP    Q       Q     P 
                 diIPAddress           P                  ConvertPAddressToString    Q       Q                              Ў1B  @    џџџџ           GETIPADDRESS           diIPAddress            ( 	                 stIPAddress    Q       Q    (            IP-address or computer name       GetIPAddress                                     Ў1B  @    џџџџ           GETRECEIVEDATASIZE           diParameter            J 	                 diSocket           J            Socket Id       GetReceiveDataSize                                     Ў1B  @    џџџџ           PLC_PRG           bInit             /                                Ў1B  @    џџџџ           RESETCALLBACK               dwEvent           Ѓ              dwFilter           Ѓ              dwOwner           Ѓ                 ResetCallback                                     Ў1B  @    џџџџ        	   TCPCLIENT           diSocket    џџџџ    p               iPort    \      p               stDestIPAddress    Q   	   127.0.0.1Q     p               bySend   	  
                   0,1,2,3,4,5,6,7,8,9,10                                                             	      
       p               byRecv   	  
                        p               bCloseClient             p               bActive             p 	                               cТCC  @    џџџџ           TCPCLIENTOPENSOCKET           diSocket                           bOptNoDelay                         
   lOptLinger                SOCKET_LINGER                   bResult                            sa                  SOCKADDRESS                      iPort                   #    Port number of TCP socket to open    stIPAddress    Q       Q            $    IP-Address of server to connect to    diMaxDataSize                   D    Max size of data to transmitt; if size = 0 default values are used       TcpClientOpenSocket                                     Ў1B  @    џџџџ           TCPRECEIVEDATA           fdRead                SOCKET_FD_SET                	   tvTimeout                SOCKET_TIMEVAL                      diSocket                       Socket Id    pbyData                       Address of data buffer 
   diDataSize                       Size of data to send 	   diTImeout            	           Timeout in seconds       TcpReceiveData                                     Ў1B  @    џџџџ           TCPSENDDATA           fdWrite                SOCKET_FD_SET                	   tvTimeout                SOCKET_TIMEVAL                      diSocket                       Socket Id    pbyData                       Address of data buffer 
   diDataSize                       Size of data to send 	   diTImeout            	           Timeout in seconds       TcpSendData                                     Ў1B  @    џџџџ        	   TCPSERVER           diSocket    џџџџ    B               iPort    \      B               Client           (diSocket := -1)    џџџџ    CLIENT_ACCEPT    B               bySend   	  
                   0,1,2,3,4,5,6,7,8,9,10                                                             	      
       B               byRecv   	  
                        B               Reply                CLIENT_REPLY    B               bCloseClient             B 	              bActive             B 
                               Ў1B  @    џџџџ           TCPSERVEROPENSOCKET           diSocket                           bResult                            sa                  SOCKADDRESS                   bOptNoDelay                         
   lOptLinger                SOCKET_LINGER                      iPort                       Port number    diMaxConnections                   /    Max possible client connections of the server    diMaxDataSize                   D    Max size of data to transmitt; if size = 0 default values are used       TcpServerOpenSocket                                     Ў1B  @    џџџџ           TCPSERVERWAITFORCONNECT           sa                  SOCKADDRESS                   ia               INADDR                   diSize                           fdRead                SOCKET_FD_SET                   fdWrite                SOCKET_FD_SET                   fdExcept                SOCKET_FD_SET                	   tvTimeout                SOCKET_TIMEVAL                      diServerSocket                       	   diTimeout            	           Timeout in seconds       TcpServerWaitForConnect                CLIENT_ACCEPT                             Ў1B  @    џџџџ           UDPCONSUMER           iPort    \      Y               stDestIPAddress    Q   	   127.0.0.1Q     Y               diRecvSocket            Y               byRecv   	  
                        Y               Reply                CLIENT_REPLY    Y               bActive             Y                                ўСCC  @    џџџџ           UDPOPENRECEIVESOCKET           diSocket            K 	              bResult             K 
              sa                  SOCKADDRESS    K                  iPort           K            Port number       UdpOpenReceiveSocket                                     Ў1B  @    џџџџ           UDPOPENSENDSOCKET           diSocket            L 	              diOption            L 
                 iPort           L            Port number       UdpOpenSendSocket                                     Ў1B  @    џџџџ           UDPPRODUCER           diSendSocket            X               iPort    \      X               stDestIPAddress    Q   	   127.0.0.1Q     X               diRecvSocket            X               bySend   	  
                   0,1,2,3,4,5,6,7,8,9,10                                                             	      
       X               bSent             X               bActive             X 	                               yА1B  @    џџџџ           UDPRECEIVEDATA           sa                  SOCKADDRESS    M               ia               INADDR    M               saSize            M                  diSocket           M            Socket Id    iPort           M            Port number, to send data    pbyData           M 	           Address of data buffer 
   diDataSize           M 
           Size of data to send       UdpReceiveData                CLIENT_REPLY                             Ў1B  @    џџџџ           UDPSENDDATA           sa                  SOCKADDRESS    N                  diSocket           N            Socket Id    iPort           N            Port number, to send data    stIPAddress    Q       Q    N            IP-address or name    pbyData           N 	           Address of data buffer 
   diDataSize           N 
           Size of data to send       UdpSendData                                     Ў1B  @    џџџџ            
    Ѓ  /   B   ( T      K    T     K   ЎT     K   МT     K   бT                 оT         +           е   е       ёт}UгГвй `чоS            Tcp/Ip (Unbenannt) PLCWinNT 3S Tcp/Ip driver    5   щ  Address IP address or hostname 
   localhost    ш  Port     А7   d   Motorola byteorder                No    Yes          е       ёт}UгГвй `чоS            Tcp/Ip CANOpen.pro PLCWinNt 3S Tcp/Ip driver    5   щ  Address IP address or hostname 
   localhost    ш  Port     А7   d   Motorola byteorder                No    Yes Э       ёт}UгГвй `чоS            Tcp/Ip  MAX405 3S Tcp/Ip driver    :   щ  Address IP address or hostname 
   194.128.128.32    ш  Port     А7   d   Motorola byteorder               No    Yes е       ёт}UгГвй `чоS            Tcp/Ip (Unbenannt) PLCWinNT 3S Tcp/Ip driver    5   щ  Address IP address or hostname 
   localhost    ш  Port     А7   d   Motorola byteorder                No    Yes   K         @   Ў1BY{      ,     ^А                     CoDeSys 1-2.2   рџџџ  ngdgdect                     Ш   X       ы      
   ђ         ѓ         ї          ј                    "          $                                                   '          (          Б          Г          Е          Й          К         Ж          Я          а          б         М          О          Р          Т          Ф         Ц         Ъ       P  Ш          Ь         Ю         в                    ~                                                                                                                                                                                 @         @         @         @         @         @  Ђ                   Ј                   M         N          O          P          `         a          t          y          z          b         c          X          d         e         _          Q          \         R          K          U         X         Z         т          ф         ц      
   ш         ъ         ь         ю         ё         я          №          ђ         ѓ      џџџџє          ѕ          ї      (                                                                        "         !          #          $                   ^          f         g          h          i          j          k         F          H         J         L          N         P         R          U         S          T          V          W          Є          Ѕ          l          o          p          q          r          s         u          о          v         І          Ї      џџџџ|         ~                  x          z      (   Љ          Ћ         %         ­          Ў          Џ         @         н          ф          и         &          №          	                   ц          ч          ш         щ          ъ         Њ          В          Д          Ќ          ­          Џ          А          З          И          О          ь          э                            I         J         K          	          L         M                                       о          P         Q          S          )          	          	                     	          +	       @  ,	       @  -	      џџџџZ	      џџџџЭЭЭЭ        џџџџШ   ђ         ѓ         ї          ј                    "          $                                                   '          (          Б          Г          Е          Й          К         Ж          Я          а          б         М          О          Р          Т          Ф         Ц         Ъ       P  Ш          Ь         Ю         в                                                                                                                                      Ђ         Ј          a          t          y          z          b         c         X          d         e         _          Q          \         R          K          U         X         Z         т          ф         ц      
   ш         ъ         ь         ю         ё         я          №          ђ         ѓ      џџџџє          ѕ          ї      (                                                                        "         !          #          $                   ^          f          g          h          i          j          k         F          H         J         L          N         P         R          U         S          T          V          W          Є         Ѕ          l          o          p          q          r          s         u          о          v         І          w          x          Ї      џџџџ|         ~                  x          z      (   Љ          Ћ         %         ­          Ў          Џ         @         м          н          р      а  с      а  у         ф          и         &          №          	                   ц          ч          ш         щ          ъ         Њ          В          Д          Ќ          ­          Џ          А          З          И          О          ы          ь          э          ў          џ                                                 I         J         K          	          L         M                                       о          P         Q          S          )          	          	                     	          +	       @  ,	       @  -	      џџџџZ	      џџџџЭЭЭЭ        џџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџџent љџџџ  , , '                                                   Ї  	   	   Name                 џџџџ
   Index                 џџ         SubIndex                 џ          Accesslevel          !         low   middle   high       Accessright          1      	   read only
   write only
   read-write       Variable    	             џџџџ
   Value                Variable       Min                Variable       Max                Variable          Л     	   Name                 џџџџ
   Index                 џџ         SubIndex                 џ          Accesslevel          !         low   middle   high       Accessright          1      	   read only
   write only
   read-write    	   Type          m         INT   UINT   DINT   UDINT   SINT   USINT   BYTE   WORD   DWORD   REAL   LREAL   STRING    
   Value                Type       Default                Type       Min                Type       Max                Type    	   Type          ~         INT   UINT   DINT   UDINT   LINT   ULINT   SINT   USINT   BYTE   WORD   DWORD   REAL   LREAL   STRING          Л     	   Name                 џџџџ
   Index                 џџ         SubIndex                 џ          Accesslevel          !         low   middle   high       Accessright          1      	   read only
   write only
   read-write    	   Type          m         INT   UINT   DINT   UDINT   SINT   USINT   BYTE   WORD   DWORD   REAL   LREAL   STRING    
   Value                Type       Default                Type       Min                Type       Max                Type    	   Type          ~         INT   UINT   DINT   UDINT   LINT   ULINT   SINT   USINT   BYTE   WORD   DWORD   REAL   LREAL   STRING          d        Member    	             џџџџ   Index-Offset                 џџ         SubIndex-Offset                 џ          Accesslevel          !         low   middle   high       Accessright          1      	   read only
   write only
   read-write       Min                Member       Max                Member            	   	   Name                 џџџџ   Member    	             џџџџ
   Value                Member    
   Index                 џџ         SubIndex                 џ          Accesslevel          !         low   middle   high       Accessright          1      	   read only
   write only
   read-write       Min                Member       Max                Member          Ї  	   	   Name                 џџџџ
   Index                 џџ         SubIndex                 џ          Accesslevel          !         low   middle   high       Accessright          1      	   read only
   write only
   read-write       Variable    	             џџџџ
   Value                Variable       Min                Variable       Max                Variable                         іџџџ                            _Dummy@    @   @@    @   @             Єя@             Єя@@   @     v@@   ; @+   ёџџџ  ЭЭЭЭЭЭЭЭ                                  v@      4@   А             v@      D@   А                       Р       @                           f@      4@     f@                v@     f@     @u@     f@        їСы           Module.Root-1__not_found__    Steuerungskonfigurationџџџџ IB  ќ"Ь!r,as% QB  X^`! @ % MB  BUAS   %    Ў1B	ЦX_           p            VAR_GLOBAL
END_VAR
                                                                                  "   ,                  MainTaskd   
     
PLC_PRG();џџџџ                
ServerTask
        TCPServer();џџџџ                
ClientTask
        TCPClient();џџџџ                ConsumerTask
        UDPConsumer();џџџџ                ProducerTask
        UDPProducer();џџџџ               Ў1B             %      start   Called when program starts    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
    Ш      stop   Called when program stops    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
    Ш      before_reset   Called before reset takes place    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
    Ш      after_reset   Called after reset took place    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
    Ш      shutdown#   Called before shutdown is performed    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
    Ш      excpt_cycletime_overflow)   Called when a cycletime overflow happened    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
    Ш      excpt_watchdog%   Software watchdog OF IEC-task expired    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
    Ш      excpt_fieldbus   Fieldbus error occurred    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
 	   Ш      excpt_ioupdate   IO-update error    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
 
   Ш      excpt_illegal_instruction   Illegal instruction    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
    Ш      excpt_access_violation   Access violation    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
    Ш      excpt_priv_instruction   Privileged instruction    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
    Ш      excpt_dividebyzero   Division BY zero    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
    Ш      excpt_fpu_error   FPU: Unspecified error    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
    Ш      excpt_fpu_denormal_operand   FPU: Denormal operand    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
    Ш      excpt_fpu_dividebyzero   FPU: Division BY zero    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
    Ш      excpt_fpu_invalid_operation   FPU: Invalid operation    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
    Ш      excpt_fpu_overflow   FPU: Overflow    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
    Ш      excpt_fpu_stack_check   FPU: Stack check    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
    Ш      after_reading_inputs   Called after reading of inputs    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
    Ш      before_writing_outputs    Called before writing of outputs    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
    Ш   
   debug_loop   Debug loop at breakpoint    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
    Ш      interrupt_1   Interrupt 1    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
 $   Ш      interrupt_2   Interrupt 2    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
 %   Ш      interrupt_3   Interrupt 3    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
 &   Ш      interrupt_4   Interrupt 4    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
 '   Ш      interrupt_5   Interrupt 5    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
 (   Ш      interrupt_6   Interrupt 6    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
 )   Ш      interrupt_7   Interrupt 7    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
 *   Ш      interrupt_8   Interrupt 8    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
 +   Ш      interrupt_9   Interrupt 9    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
 ,   Ш      interrupt_10   Interrupt 10    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
 -   Ш      interrupt_11   Interrupt 11    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
 .   Ш      interrupt_12   Interrupt 12    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
 /   Ш      interrupt_13   Interrupt 13    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
 0   Ш      interrupt_14   Interrupt 14    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
 1   Ш      interrupt_15   Interrupt 15    h   FUNCTION systemevent: DWORD
VAR_INPUT
	dwEvent: DWORD;
	dwFilter: DWORD;
	dwOwner: DWORD;
END_VAR
 2   Ш   $ћџџџ                         ЭЭЭЭЭЭЭЭ           Standard n)К>	n)К>      ЭЭЭЭЭЭЭЭ                         	ЁуYD     leorD ge           VAR_CONFIG
END_VAR
  јейHвй                                                                            I   |0|0 @?    @   Arial @        @           єџџџ                               ї      џ   џџџ  Ь3 џџџ   џ џџџ     
    @џ  џџџ     @      DEFAULT             System      I   |0|0 @?    @   Arial @        @           єџџџ                      )   hh':'mm':'ss @                             dd'-'MM'-'yyyy @       '      , n n Ћ           CLIENT_ACCEPT Ў1B	Ў1B            ЌЌ        ]   TYPE CLIENT_ACCEPT :
STRUCT
	diSocket:DINT;
	stIPAddress:STRING(20);
END_STRUCT
END_TYPE                , А А            CLIENT_REPLY Ў1B	Ў1B      drs  htn        n   TYPE CLIENT_REPLY :
STRUCT
	diBytesReceived:DINT;
	stIPAddressTransmitter:STRING(20);
END_STRUCT
END_TYPE              P   , Н Ц Ћ?           ConvertPAddressToString  Ў1B	Ў1B                   ц   FUNCTION ConvertPAddressToString : STRING
(*	Convert the IP-Address to a string in dot-notation, e.g. '192.168.100.2' .
	Return:	IP-address
 *)
VAR_INPUT
	diIPAddress:DINT;
END_VAR
VAR
	iadr:INADDR;
	stIP:STRING;
END_VARg   iadr.S_addr := diIPAddress;
SysSockInetNtoa(iadr, stIP, SIZEOF(stIP));
ConvertPAddressToString:=stIP;               (   , " їџ7О           GetIPAddress Ў1B	Ў1B      e   caos        д   FUNCTION GetIPAddress : DINT
(*	Convert IP-Address from string to address.
	Return:	IP-address
 *)
VAR_INPUT
	stIPAddress:STRING;		(* IP-address or computer name *)
END_VAR
VAR
	diIPAddress:DINT;
END_VARГ   diIPAddress := SysSockInetAddr(stIPAddress);
IF diIPAddress = SOCKET_INADDR_NONE THEN
	diIPAddress := SysSockGetHostByName(ADR(stIPAddress));
END_IF
GetIPAddress:=diIPAddress;               J   ,   kО           GetReceiveDataSize  Ў1B	Ў1B        q ` Д<          FUNCTION GetReceiveDataSize : DINT
(* Function to get received number of bytes in socket, without removing it from the socket.
	Return:	Number of bytes received
 *)	
VAR_INPUT
	diSocket	: DINT;		(* Socket Id *)
END_VAR
VAR
	diParameter:DINT;
END_VARЈ   diParameter:=0;
IF SysSockIoctl(diSocket, SOCKET_FIONREAD, ADR(diParameter)) = 1 THEN
	GetReceiveDataSize := diParameter;
ELSE
	GetReceiveDataSize := 0;
END_IF

               /   , n  ъ           PLC_PRG Ў1B	Ў1B                      +   PROGRAM PLC_PRG
VAR
	bInit:BOOL;
END_VARo   IF NOT bInit THEN
	SysCallbackRegister(INDEXOF(ResetCallback), EVENT_BEFORE_RESET);
	bInit := TRUE;
END_IF
               Ѓ  , з ух           ResetCallback Ў1B	Ў1B                      t   FUNCTION ResetCallback : DWORD
VAR_INPUT
	dwEvent:DWORD;
	dwFilter:DWORD;
	dwOwner:DWORD;
END_VAR
VAR
END_VARщ  IF dwEvent = EVENT_BEFORE_RESET THEN
	IF TCPServer.diSocket <> -1 THEN
		SysSockClose(TCPServer.diSocket);
	END_IF
	IF (TCPServer.Client.diSocket <> -1) THEN
		SysSockClose(TCPServer.Client.diSocket);
	END_IF
	IF TCPClient.diSocket <> -1 THEN
		SysSockClose(TCPClient.diSocket);
	END_IF
	IF UDPProducer.diSendSocket <> -1 THEN
		SysSockClose(UDPProducer.diSendSocket);
	END_IF
	IF UDPConsumer.diRecvSocket <> -1 THEN
		SysSockClose(UDPConsumer.diRecvSocket);
	END_IF
END_IF               p   , ѓ  цl        	   TCPClient cТCC	cТCC       :RR[01         ћ   PROGRAM TCPClient
VAR
	diSocket : DINT := -1;
	iPort : INT:=4444;
	stDestIPAddress : STRING := '127.0.0.1';
	bySend : ARRAY[0..10] OF BYTE := 0,1,2,3,4,5,6,7,8,9,10;
	byRecv : ARRAY[0..10] OF BYTE;
	bCloseClient: BOOL;
	bActive: BOOL;
END_VAR  IF bActive THEN
	IF diSocket = -1 THEN
		diSocket := TcpClientOpenSocket(iPort, stDestIPAddress, 1000);
	END_IF

	IF  diSocket <> -1 THEN
		TcpReceiveData(diSocket, ADR(byRecv), SIZEOF(byRecv), 5);
		TcpSendData(diSocket, ADR(bySend), SIZEOF(bySend), 1);
	END_IF

	IF bCloseClient THEN
		bCloseClient := FALSE;
		SysSockClose(diSocket:=diSocket);
		diSocket := -1;
	END_IF
END_IF
                  , , , A           TcpClientOpenSocket  БD	Ў1B      цццц        с  FUNCTION TcpClientOpenSocket : DINT
(*	Open TCP client socket to connect to server.
	Return:	Socket-Id for connection session
*)
VAR_INPUT
	iPort:INT;					(* Port number of TCP socket to open *)
	stIPAddress:STRING;		(* IP-Address of server to connect to *)
	diMaxDataSize:DINT;		(* Max size of data to transmitt; if size = 0 default values are used *)
END_VAR
VAR
	diSocket:DINT;
	bOptNoDelay:BOOL;
	lOptLinger:SOCKET_LINGER;
	bResult:BOOL;
	sa:SOCKADDRESS;
END_VARз  diSocket:=SysSockCreate(SOCKET_AF_INET, SOCKET_STREAM, 0);
IF diSocket <> SOCKET_INVALID THEN
	SysSockSetOption(diSocket, SOCKET_SOL, SOCKET_SO_SNDBUF, ADR(diMaxDataSize), SIZEOF(diMaxDataSize));
	SysSockSetOption(diSocket, SOCKET_SOL, SOCKET_SO_RCVBUF, ADR(diMaxDataSize), SIZEOF(diMaxDataSize));
	lOptLinger.l_onoff:=0;
	lOptLinger.l_linger:=0;
	SysSockSetOption(diSocket,	SOCKET_SOL, SOCKET_SO_LINGER, ADR(lOptLinger), SIZEOF(lOptLinger));
	bOptNoDelay:=TRUE;
	SysSockSetOption(diSocket,	SOCKET_IPPROTO_TCP, SOCKET_TCP_NODELAY, ADR(bOptNoDelay), SIZEOF(bOptNoDelay));

	sa.sin_family:=SOCKET_AF_INET;
	sa.sin_addr:=GetIPAddress(stIPAddress);
	IF sa.sin_addr <> SOCKET_INADDR_NONE THEN
		sa.sin_port:=SysSockHtons(iPort);
		IF SysSockConnect(diSocket, ADR(sa), SIZEOF(sa)) = FALSE THEN
			SysSockClose(diSocket);
			diSocket:=SOCKET_INVALID;
		END_IF
	ELSE
		SysSockClose(diSocket);
		diSocket:=SOCKET_INVALID;
	END_IF
END_IF
TcpClientOpenSocket:=diSocket;
                  ,  Д 2ё           TcpReceiveData  Ў1B	Ў1B      Ј ф          m  FUNCTION TcpReceiveData : DINT
(*	Receive data from a tcp socket.
	Return:	Number of bytes received
*)
VAR_INPUT
	diSocket:DINT;		(* Socket Id *)
	pbyData:DWORD;		(* Address of data buffer *)
	diDataSize:DINT;		(* Size of data to send *)
	diTImeout : DINT;		(* Timeout in seconds *)
END_VAR
VAR
	fdRead:SOCKET_FD_SET;
	tvTimeout:SOCKET_TIMEVAL;
END_VAR  tvTimeout.tv_sec := diTimeout ;
tvTimeout.tv_usec := 0;
fdRead.fd_count := 1;
fdRead.fd_array[0] := diSocket;
IF (SysSockSelect(SOCKET_FD_SETSIZE, ADR(fdRead), 0, 0, ADR(tvTimeout)) > 0) THEN
	TcpReceiveData:=SysSockRecv(diSocket, pbyData, diDataSize, 0);
END_IF                  , c  xО           TcpSendData  Ў1B	Ў1B                      a  FUNCTION TcpSendData : DINT
(*	Send data via TCP socket.
	Return:	Number of bytes sent
*)
VAR_INPUT
	diSocket:DINT;		(* Socket Id *)
	pbyData:DWORD;		(* Address of data buffer *)
	diDataSize:DINT;		(* Size of data to send *)
	diTImeout : DINT;		(* Timeout in seconds *)
END_VAR
VAR
	fdWrite:SOCKET_FD_SET;
	tvTimeout:SOCKET_TIMEVAL;
END_VAR  tvTimeout.tv_sec := diTimeout ;
tvTimeout.tv_usec := 0;
fdWrite.fd_count := 1;
fdWrite.fd_array[0] := diSocket;
IF (SysSockSelect(SOCKET_FD_SETSIZE, 0, ADR(fdWrite), 0, ADR(tvTimeout)) > 0) THEN
	TcpSendData:=SysSockSend(diSocket, pbyData, diDataSize, 0);
END_IF               B   ,   N        	   TCPServer oЧX_	Ў1B                        PROGRAM TCPServer
VAR
	diSocket : DINT := -1;
	iPort : INT:=4444;
	Client : CLIENT_ACCEPT := (diSocket := -1);
	bySend : ARRAY[0..10] OF BYTE := 0,1,2,3,4,5,6,7,8,9,10;
	byRecv : ARRAY[0..10] OF BYTE;
	Reply : CLIENT_REPLY;
	bCloseClient: BOOL;
	bActive: BOOL;
END_VAR  IF bActive THEN
	IF diSocket = -1 THEN
		diSocket := TcpServerOpenSocket(iPort, 10, 1000);
	END_IF

	IF  Client.diSocket = -1 THEN
		Client := TcpServerWaitForConnect(diSocket, 4);
	END_IF

	IF  Client.diSocket <> -1 THEN
		TcpSendData(Client.diSocket, ADR(bySend), SIZEOF(bySend), 1);
		(*TcpReceiveData(Client.diSocket, ADR(byRecv), SIZEOF(byRecv), 5);*)
	END_IF

	IF bCloseClient THEN
		bCloseClient := FALSE;
		SysSockClose(diSocket:=Client.diSocket);
		Client.diSocket := -1;
	END_IF
END_IF
                  ,  ? п           TcpServerOpenSocket  Ў1B	Ў1B        Аa D        Ж  FUNCTION TcpServerOpenSocket : DINT
(*	Open a TCP server socket.
	Return:	Main Socket Id
*)
VAR_INPUT
	iPort:INT;						(* Port number *)
	diMaxConnections:DINT;		(* Max possible client connections of the server *)
	diMaxDataSize:DINT;			(* Max size of data to transmitt; if size = 0 default values are used *)
END_VAR
VAR
	diSocket:DINT;
	bResult:BOOL;
	sa:SOCKADDRESS;
	bOptNoDelay:BOOL;
	lOptLinger:SOCKET_LINGER;
END_VARћ  diSocket:=SysSockCreate(SOCKET_AF_INET, SOCKET_STREAM, 0);
IF diSocket <> SOCKET_INVALID THEN
(*
	IF diMaxDataSize <> 0 THEN
		SysSockSetOption(diSocket, SOCKET_SOL, SOCKET_SO_SNDBUF, ADR(diMaxDataSize), SIZEOF(diMaxDataSize));
		SysSockSetOption(diSocket, SOCKET_SOL, SOCKET_SO_RCVBUF, ADR(diMaxDataSize), SIZEOF(diMaxDataSize));
	END_IF
	lOptLinger.l_onoff:=0;
	lOptLinger.l_linger:=0;
	SysSockSetOption(diSocket,	SOCKET_SOL, SOCKET_SO_LINGER, ADR(lOptLinger), SIZEOF(lOptLinger));
	bOptNoDelay:=TRUE;
	SysSockSetOption(diSocket,	SOCKET_IPPROTO_TCP, SOCKET_TCP_NODELAY, ADR(bOptNoDelay), SIZEOF(bOptNoDelay));
*)

	sa.sin_family:=SOCKET_AF_INET;
	sa.sin_addr:=SOCKET_INADDR_ANY;
	sa.sin_port:=SysSockHtons(iPort);
	bResult:=SysSockBind(diSocket, ADR(sa), SIZEOF(sa));
	IF bResult = FALSE THEN
		diSocket:=SOCKET_INVALID;
	ELSE
		bResult:=SysSockListen(diSocket, diMaxConnections);
		IF bResult = FALSE THEN
			diSocket:=SOCKET_INVALID;
		END_IF
	END_IF
END_IF
TcpServerOpenSocket:=diSocket;                  ,   1           TcpServerWaitForConnect  Ў1B	Ў1B      a/`/`            FUNCTION TcpServerWaitForConnect : CLIENT_ACCEPT
(*	Wait for a TCP client to connect.
	ATTENTION:  Function is blocking, until a client tries to connect!
	Return:	diSocket : Socket Id for connection session
				stIPAddress : IP-Address of connected client
*)
VAR_INPUT
	diServerSocket:DINT;
	diTimeout : DINT;	(* Timeout in seconds *)
END_VAR
VAR
	sa:SOCKADDRESS;
	ia:INADDR;
	diSize:DINT;
	fdRead: SOCKET_FD_SET;
	fdWrite:SOCKET_FD_SET;
	fdExcept:SOCKET_FD_SET;
	tvTimeout:SOCKET_TIMEVAL;
END_VAR  tvTimeout.tv_sec := diTimeout ;
tvTimeout.tv_usec := 0;
fdRead.fd_count := 1;
fdRead.fd_array[0] := diServerSocket;
IF (SysSockSelect(SOCKET_FD_SETSIZE, ADR(fdRead), 0, 0, ADR(tvTimeout)) > 0) THEN
	diSize:=SIZEOF(sa);
	TcpServerWaitForConnect.diSocket:=SysSockAccept(diServerSocket, ADR(sa), ADR(diSize));
	ia.S_addr:=DINT_TO_DWORD(sa.sin_addr);
	SysSockInetNtoa(ia, TcpServerWaitForConnect.stIPAddress, SIZEOF(TcpServerWaitForConnect.stIPAddress));
ELSE
	TcpServerWaitForConnect.diSocket := -1;
END_IF
               Y   ,   lѓи           UDPConsumer ўСCC	ўСCC      7,9,;bS        С   PROGRAM UDPConsumer
VAR
	iPort : INT:=4444;
	stDestIPAddress : STRING := '127.0.0.1';
	diRecvSocket: DINT;
	byRecv : ARRAY[0..10] OF BYTE;
	Reply : CLIENT_REPLY;
	bActive: BOOL;
END_VARт   IF bActive THEN
	IF diRecvSocket = 0 THEN
		diRecvSocket := UdpOpenReceiveSocket(iPort);
	END_IF
	
	IF diRecvSocket > 0 THEN
		Reply := UdpReceiveData(diRecvSocket, iPort, ADR(byRecv), SIZEOF(byRecv));
	END_IF
END_IF
               K   ,   д           UdpOpenReceiveSocket  Ў1B	Ў1B      D_R             к   FUNCTION UdpOpenReceiveSocket : DINT
(*	Open socket to receive data via UDP.
	Return:	Socket Id
*)
VAR_INPUT
	iPort:INT;		(* Port number *)
END_VAR
VAR
	diSocket:DINT;
	bResult:BOOL;
	sa:SOCKADDRESS;
END_VAR1  diSocket:=SysSockCreate(SOCKET_AF_INET, SOCKET_DGRAM, 0);
sa.sin_family:=SOCKET_AF_INET;
sa.sin_addr:=SOCKET_INADDR_ANY;
sa.sin_port:=SysSockHtons(iPort);
bResult:=SysSockBind(diSocket, ADR(sa), SIZEOF(sa));
IF bResult = FALSE THEN
	diSocket:=SOCKET_INVALID;
END_IF
UdpOpenReceiveSocket:=diSocket;               L   , w H lШ           UdpOpenSendSocket  Ў1B	Ў1B      NDARVA
	        У   FUNCTION UdpOpenSendSocket : DINT
(*	Open socket to send data via UDP.
	Return:	Socket Id
*)
VAR_INPUT
	iPort:INT;		(* Port number *)
END_VAR
VAR
	diSocket:DINT;
	diOption:DINT;
END_VARs  diSocket:=SysSockCreate(SOCKET_AF_INET, SOCKET_DGRAM, 0);
IF diSocket = SOCKET_INVALID THEN
	UdpOpenSendSocket:=SOCKET_INVALID;
ELSE
(*
	diOption:=1;
	IF SysSockSetOption(diSocket, SOCKET_SOL, SOCKET_SO_BROADCAST, ADR(diOption), SIZEOF(diOption)) = FALSE THEN
		UdpOpenSendSocket:=SOCKET_INVALID;
	ELSE
*)
		UdpOpenSendSocket:=diSocket;
(*
	END_IF
*)
END_IF               X   ,     ѓl           UDPProducer yА1B	yА1B      3,5,7,9,        щ   PROGRAM UDPProducer
VAR
	diSendSocket : DINT;
	iPort : INT:=4444;
	stDestIPAddress : STRING := '127.0.0.1';
	diRecvSocket: DINT;
	bySend : ARRAY[0..10] OF BYTE := 0,1,2,3,4,5,6,7,8,9,10;
	bSent: BOOL;
	bActive: BOOL;
END_VAR  IF bActive THEN
	IF diSendSocket = 0 THEN
		diSendSocket := UdpOpenSendSocket(iPort);
	END_IF
	
	IF diSendSocket > 0 AND bSent THEN
		bSent := FALSE;
		UdpSendData(diSendSocket, iPort, stDestIPAddress, ADR(bySend), SIZEOF(bySend));
	END_IF
END_IF
               M   , 6 m Ї           UdpReceiveData  Ў1B	Ў1B        АA (        д  FUNCTION UdpReceiveData : CLIENT_REPLY
(* Function to receive data via UDP protocol.
	Return:	diBytesReceived:Number of bytes received
				stIPAddressTransmitter: IP-address of client, that sent the data
 *)	
VAR_INPUT
	diSocket:DINT;		(* Socket Id *)
	iPort:INT;				(* Port number, to send data *)
	pbyData:DWORD;		(* Address of data buffer *)
	diDataSize:DINT;		(* Size of data to send *)
END_VAR
VAR
	sa:SOCKADDRESS;
	ia:INADDR;
	saSize:DINT;
END_VARћ   UdpReceiveData.diBytesReceived:=SysSockRecvFrom(diSocket, pbyData, diDataSize, 0, ADR(sa), SIZEOF(sa));
ia.S_addr:=DINT_TO_DWORD(sa.sin_addr);
SysSockInetNtoa(ia, UdpReceiveData.stIPAddressTransmitter, SIZEOF(UdpReceiveData.stIPAddressTransmitter));               N   , ѓ ! км           UdpSendData  Ў1B	Ў1B                        FUNCTION UdpSendData : DINT
(* Function to send data via UDP protocol.
	Return:	Number of bytes realy sent
*)	
VAR_INPUT
	diSocket:DINT;		(* Socket Id *)
	iPort:INT;				(* Port number, to send data *)
	stIPAddress:STRING;		(* IP-address or name *)
	pbyData:DWORD;		(* Address of data buffer *)
	diDataSize:DINT;		(* Size of data to send *)
END_VAR
VAR
	sa:SOCKADDRESS;
END_VAR  sa.sin_family:=SOCKET_AF_INET;
IF stIPAddress <> '' THEN
	sa.sin_addr:=GetIPAddress(stIPAddress);
ELSE
	sa.sin_addr:=SOCKET_INADDR_BROADCAST;
END_IF
sa.sin_port:=SysSockHtons(iPort);
UdpSendData:=SysSockSendTo(diSocket, pbyData, diDataSize, 0, ADR(sa), SIZEOF(sa));
                 §џџџ, Е % #         '   SysLibSockets.lib*2.6.14 13:06:08 @ ZS"   Standard.lib*2.6.14 11:37:46 @ъES(   SYSLIBCALLBACK.LIB*2.6.14 13:06:08 @ ZS   Ј   SysSockAccept @      INADDR       SOCK_IP_MREQ       SOCKADDRESS       SOCKET_FD_SET       SOCKET_KEEPALIVE       SOCKET_LINGER       SOCKET_TIMEVAL                   SysSockBind @           SysSockClose @           SysSockConnect @           SysSockCreate @           SysSockGetHostByName @           SysSockGetHostName @           SysSockGetLastError @          SysSockGetLastErrorSync @          SysSockGetOption @           SysSockHtonl @           SysSockHtons @           SysSockInetAddr @           SysSockInetNtoa @           SysSockIoctl @           SysSockListen @           SysSockNtohl @           SysSockNtohs @           SysSockRecv @           SysSockRecvFrom @           SysSockSelect @           SysSockSend @           SysSockSendTo @           SysSockSetIPAddress @           SysSockSetOption @           SysSockShutdown @              Globale_Variablen @              CONCAT @                	   CTD @        	   CTU @        
   CTUD @           DELETE @           F_TRIG @        
   FIND @           INSERT @        
   LEFT @        	   LEN @        	   MID @           R_TRIG @           REPLACE @           RIGHT @           RS @        	   RTC @        
   SEMA @           SR @        	   TOF @        	   TON @           TP @               b   SysCallbackRegister @   	   RTS_EVENT       RTS_EVENT_FILTER       RTS_EVENT_SOURCE                   SysCallbackUnregister @                              mphб               2 ѓ  ѓ           џџџџџџџџџџџџџџџџ  
             њџџџ,     Hq        јџџџ   С8СрХаФ                      POUs               Tcp specific                 TcpClientOpenSocket                     TcpReceiveData                     TcpSendData                     TcpServerOpenSocket                     TcpServerWaitForConnect     џџџџ              Udp specific                 UdpOpenReceiveSocket  K                   UdpOpenSendSocket  L                   UdpReceiveData  M                   UdpSendData  N   џџџџ                ConvertPAddressToString  P                   GetIPAddress  (                   GetReceiveDataSize  J                   PLC_PRG  /                   ResetCallback  Ѓ               	   TCPClient  p               	   TCPServer  B                   UDPConsumer  Y                   UDPProducer  X   џџџџ           
   Data types                 CLIENT_ACCEPT                    CLIENT_REPLY     џџџџ             Visualizations  џџџџ             Global Variables  џџџџ                                               #              n)К>Ш      1                                   Ш       i+      DH                	   localhost            P      	   localhost            P      	   localhost            P     yP~A    ћФAЄ