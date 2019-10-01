pdev_FIRST_DEVICE_ID_USED           = -128;  # [128]
pdev_EMPTY                          = pdev_FIRST_DEVICE_ID_USED;


"""
* This 'spare' set were the Thorn MINERVA devices
When these are used REMEMBER MXSPEAK ANNEX.
"""
pdev_P80SB                          = -116;  # [140] Addressable sounder base
pdev_P80SW_R                        = -115;  # [141] addressable wall sounder (White / Red)
pdev_P85SR                          = -114;  # [142] Addressable wall sounder IP
pdev_P80AIB                         = -113;  # [143] Sounder Beacon Base
pdev_P80AIW_R                       = -112;  # [144] Wall sounder beacon (White / Red)
pdev_P85AIR                         = -111;  # [145] wall sounder beacon IP
pdev_P80AVB                         = -110;  # [146] sounder base beacon C-3-8
pdev_P81AVB                         = -109;  # [147] sounder base beacon C-3-15
pdev_P80AVW_R                       = -108;  # [148] wall sounder beacon (white / red)
pdev_P85AVR                         = -107;  # [149] wall sounder beacon IP
                                         
"""                                           
* Pseudo Loop Devices                       
"""                                          #
pdev_LOOP_CONTROL                   = -62,   # [194]
pdev_LOOP_CIRCUIT                   = -61,   # [195]
                                         #
                                         #
"""                                        
* NOSEX Loop Devices                       
"""                                       
pdev_801_H                          = -60;   # [196] norm EN heat detector
pdev_801_CH                         = -59;   # [197] norm EN CO heat detector
pdev_801_PH                         = -58;   # [198] norm EN photo heat detector
pdev_801_I                          = -57;   # [199] norm EN ion detector
pdev_811_H                          = -56;   # [200] norm marine heat detector
pdev_811_CH                         = -55;   # [201] norm marine CO heat detector
pdev_811_PH                         = -54;   # [202] norm marine photo heat detector
pdev_812_H                          = -53;   # [203] norm UL heat detector
pdev_812_PH                         = -52;   # [204] norm UL photo heat detector
pdev_812_I                          = -51;   # [205] norm UL ion detector
pdev_812_IA                         = -50;   # [206] norm UL ion detector for high altitudes
pdev_AMP_800                        = -49;   # [207] audio AMPlifier
pdev_CSM_800                        = -48;   # [208] audio Channel Select Module
pdev_GAR_800                        = -47;   # [209] Gas/Agent Release station
pdev_GARA_800                       = -46;   # [210] Gas/Agent Release & Abort station
pdev_LPS_800                        = -45;   # [211] Loop Powered Sounder
pdev_MIM_800                        = -44;   # [212] Mini Input Monitor
pdev_MIM_800_US                     = -43;   # [213] Mini Input Monitor for US
pdev_PSM_800                        = -42;   # [214] APSU800 / Power Supply Monitor/Module. Now APM800 !!!
pdev_RIM_800                        = -41;   # [215] Relay Interface Module
pdev_RMS_800                        = -40;   # [216] indoor pull station just for US
pdev_SNM_800                        = -39;   # [217] Sounder/Notification Module
pdev_S271f_PLUS                     = -38;   # [218] flame detector
pdev_LAV_800                        = -37;   # [219] extingusher control (Loesch Ansteuerung Vds)
pdev_CP_820                         = -36;   # [220] indoor break glas Call Point
pdev_CP_830                         = -35;   # [221] outdoor break glas Call Point
pdev_CP_820_M                       = -34;   # [222] indoor break glas Call Point for Marine
pdev_CP_830_M                       = -33;   # [223] outdoor break glas Call Point for Marine
pdev_DIN_820                        = -32;   # [224] indoor break glas call point for DIN
pdev_DIN_830                        = -31;   # [225] outdoor break glas call point for DIN
pdev_DIM_800_STD                    = -30;   # [226] Detector Input Monitor
pdev_DIM_800_STD_US                 = -29;   # [227] Detector Input Monitor for US
pdev_DIM_800_INTR                   = -28;   # [228] Detector Input Monitor for interrupt
pdev_DIM_800_INTR_US                = -27;   # [229] Detector Input Monitor for interrupt and for US
pdev_CIM_800_STD                    = -26;   # [230] Contact Input Monitor
pdev_CIM_800_STD_US                 = -25;   # [231] Contact Input Monitor for US
pdev_CIM_800_INTR                   = -24;   # [232] Contact Input Monitor for interrupt
pdev_CIM_800_INTR_US                = -23;   # [233] Contact Input Monitor for interrupt and for US                              
"""                                      
* Digital Devices                      
"""                                    
pdev_DIGITAL_INPUT_NORMAL           = -22;   # [234]
pdev_DIGITAL_INPUT_TOGGLE           = -21;   # [235]
pdev_DIGITAL_OUTPUT                 = -20;   # [236]
pdev_DIGITAL_VISUAL_OUTPUT          = -19;   # [237]
pdev_DIGITAL_TOGGLE_OUTPUT          = -18;   # [238]
pdev_DIGITAL_SUPERVISED_OUTPUT      = -17;   # [239]
pdev_ZONAL_DISPLAY                  = -16;   # [240]
                                     
# test device for SYSTEM SENSOR loop typ;
pdev_SYSTEM_SENSOR_TEST_DEVICE      = -15;   # [240] Test Device for System Sensor
pdev_812_ID                         = -14;   # [241] For US, UL Approved
pdev_812_PD                         = -13;   # [242] For US, UL Approved
pdev_SPARE_SLOT                     = -12;   # [243] TEL 800 Removed
pdev_VESDA_INTERFACE                = -11;   # [244] Detector, For EN54, For UK & Germany
pdev_SPARE_SLOT_1                   = -10;   # [245] MIM801 Removed
pdev_MIM_800_INTR                   = -9;    # [246] Mini Input Monitor with Interrupt
pdev_813_P                          = -8;    # [247] 801PH Lite detector

pdev_DEVICE_ID_FOREIGN = 0x7d,  # [125] Types from 'Foreign' Panels, e.g. Minerva
pdev_DEVICE_ID_INVALID = 0x7e,  # [126]
pdev_DEVICE_ID_ALL     = 0x7f   # [127]
