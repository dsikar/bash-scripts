spkd_ID_INVALID                                   = 0;   # 0x00 - SPECIAL
spkd_ID_STATUS_ENQUIRY                            = 1;   # 0x01 - MPIM
spkd_ID_STATUS_MESSAGE                            = 2;   # 0x02 - MPIM
spkd_ID_VDR_SENTENCE                              = 3;   # 0x03 - Voyage Data Recorder (VDR)
spkd_ID_POINT_STATUS_UPDATE_EXTENDED              = 4;   # 0x04 - similar to spkd_ID_POINT_STATUS_UPDATE but using different data

spkd_ID_REMOTE_NETWORK_FAULT_REQUEST              = 5;   # 0x05 - About TLI not to TLI
spkd_ID_REMOTE_NETWORK_FAULT_REPORT               = 6;   # 0x06 - About TLI not to TLI

#network card specific
spkd_ID_NET_CONFIG_REQUEST                        = 7;   # 0x07 - TLI800
spkd_ID_NET_CONFIG_RESPONSE                       = 8;   # 0x08 - TLI800
spkd_ID_NET_FAULT_REQUEST                         = 9;   # 0x09 - TLI800
spkd_ID_NET_FAULT_REPORT                          = 10;  # 0x0a - TLI800
spkd_ID_NET_VERSION_REQUEST                       = 11;  # 0x0b - TLI800
spkd_ID_NET_VERSION_RESPONSE                      = 12;  # 0x0c - TLI800

#Filnet network card specific                       ;  #
spkd_ID_FILNET_EMERGENCY                          = 14;  # 0x0e - Filnet
spkd_ID_FILNET_CONFIG_RESPONSE                    = 15;  # 0x0f - Filnet
spkd_ID_FILNET_CONFIG_REQUEST                     = 16;  # 0x10 - Filnet
spkd_ID_FILNET_FAULT_REQUEST                      = 17;  # 0x11 - Filnet
spkd_ID_FILNET_FAULT_REPORT                       = 18;  # 0x12 - Filnet
spkd_ID_FILNET_STATUS_LOG_REQUEST                 = 19;  # 0x13 - Filnet
spkd_ID_FILNET_STATUS_LOG_RESPONSE                = 20;  # 0x14 - Filnet
spkd_ID_FILNET_ALARM_IN_PANEL_REPORT              = 21;  # 0x15 - Filnet

#Packets for Consys to get the panel details
spkd_ID_REQUEST_PANEL_DETAILS                     = 26;  # 0x1a
spkd_ID_PANEL_DETAILS                             = 27;  # 0x1b

spkd_ID_SET_MPIM_MODE                             = 32;  # 0x20 - MPIM
spkd_ID_BEEP                                      = 33;  # 0x21 - MPIM
spkd_ID_XBUS_WRITE                                = 34;  # 0x22 - MPIM
#used if only a few points need to be set
spkd_ID_XBUS_QUICK_PULSE_SETUP                    = 35;  # 0x23 - MPIM

spkd_ID_XBUS_FEW_POINTS_CHANGED                   = 37;  # 0x25 - MPIM
spkd_ID_WRITE_LCD                                 = 38;  # 0x26 - MPIM
spkd_ID_PRINT                                     = 39;  # 0x27 - MPIM
spkd_ID_SERIAL_DATA                               = 40;  # 0x28 - MPIM
spkd_ID_UIF_KEY_PACKET                            = 41;  # 0x29 - MPIM
spkd_ID_LCD_TEST                                  = 42;  # 0x2a - MPIM
spkd_ID_GMPIM_DISPLAY_LOGO                        = 43;  # 0x2b - GMPIM
spkd_ID_LOAD_LCD_CODEPAGE                         = 44;  # 0x2c - MPIM
spkd_ID_GMPIM_DISPLAY_TIME                        = 45;  # 0x2d - GMPIM
# Used on profile flexible based panels when the MCPU is dead
# and the local IO processor handles emergency statuses broadcast
# to the GUI over RBUS.
spkd_ID_EMERGENCY_MODE_STATUSES                   = 46;  # 0x2e – Local IO (PLX800 firmware) on PFI800 main board.

spkd_ID_MPIM_BAUD_RATE_CHANGE                     = 65;  # 0x41 - MPIM

#Digital Points Output Packet Types
spkd_ID_XBUS_OUTPUT_ON                            = 66;  # 0x42 - MPIM
spkd_ID_XBUS_OUTPUT_OFF                           = 67;  # 0x43 - MPIM
spkd_ID_XBUS_OUTPUT_PULSE_1                       = 68;  # 0x44 - MPIM
spkd_ID_XBUS_OUTPUT_PULSE_2                       = 69;  # 0x45 - MPIM

#configure pulse pattern Packet                     ;  #
spkd_ID_XBUS_SET_PULSE_PATTERN                    = 70;  # 0x46 - MPIM

#Digital Points Input Packet Types
spkd_ID_XBUS_INPUT_CONFIG_LOW                     = 71;   # 0x47 - MPIM
spkd_ID_XBUS_INPUT_CONFIG_HIGH                    = 72;   # 0x48 - MPIM
spkd_ID_XBUS_INPUT_REPLY_LOW                      = 73;   # 0x49 - MPIM
spkd_ID_XBUS_INPUT_REPLY_HIGH                     = 74;   # 0x4a - MPIM
spkd_ID_SOFT_RESET_REQ                            = 98;   # 0x62 - MPIM
spkd_ID_SOFT_RESET_ACK                            = 99;   # 0x63 - MPIM

spkd_ID_REMOTE_STRING_REQUEST_BY_PROXY            = 116;  # 0x74 - MX Speak

spkd_ID_TEST_SELF_CHECK_RESULTS                   = 117;  # 0x75
spkd_ID_MPIM_REQUESTS_DISPLAY_REFRESH             = 118;  # 0x76 - MPIM
spkd_ID_MPIM_INFO_REQUEST                         = 119;  # 0x77 - MPIM
spkd_ID_MPIM_INFO_REPLY                           = 120;  # 0x78 - MPIM

spkd_ID_MPIM_VERSION_INFO_REQUEST                 = 122;  # 0x7a - MPIM
spkd_ID_MPIM_VERSION_INFO_REPLY                   = 123;  # 0x7b - MPIM
spkd_ID_LCD_BACKLIGHT_REQUEST                     = 124;  # 0x7c - MPIM

spkd_ID_MPIM_HEART_BEAT                           = 126;  # 0x7e - MPIM (Defunct)
spkd_ID_ILLEGAL_COMMAND                           = 127;  # 0x7f - MPIM


#These packet IDs are fixed and their values may be known
#to external developers do NOT change them.
spkd_ID_NET_SUPERVISOR_MODE                       = 128;  # 0x80 - MX Speak
spkd_ID_NET_SUPERVISED_PANEL_MODE                 = 129;  # 0x81 - MX Speak
spkd_ID_SYSTEM_REMOTE_USER_INTERFACE_PRESENT      = 130;  # 0x82
spkd_ID_EVENT_ACTION_ZONE_STATE_REQUEST           = 131;  # 0x83 - MX Speak
spkd_ID_EVENT_ACTION_ZONE_INFORMATION_TRANSFER    = 132;  # 0x84 - MX Speak
spkd_ID_POINT_INFO_BITMAP_REQUEST                 = 133;  # 0x85 - MX Speak
spkd_ID_POINT_INFO_BITMAP_REPLY                   = 134;  # 0x86 - MX Speak
spkd_ID_NETWORK_POINT_COMMAND                     = 135;  # 0x87 - MX Speak
spkd_ID_NETWORK_POINT_COMMAND_REPLY               = 136;  # 0x88 - MX Speak
spkd_ID_EVENT                                     = 137;  # 0x89 - MX Speak

spkd_ID_LOG_EVENT_DATA                            = 139;  # 0x8b - MX Speak
spkd_ID_LOG_EVENT_COUNTER_DATA                    = 140;  # 0x8c
spkd_ID_LOG_EVENT_ACCEPTANCE                      = 141;  # 0x8d
spkd_ID_LOG_REGISTER_CLIENT                       = 142;  # 0x8e
spkd_ID_LOG_DEREGISTER_CLIENT                     = 143;  # 0x8f
spkd_ID_LOG_PAUSE_EVENT_DATA                      = 144;  # 0x90
spkd_ID_LOG_UNPAUSE_EVENT_DATA                    = 145;  # 0x91
spkd_ID_LOG_ACKNOWLEDGE                           = 146;  # 0x92 - MX Speak
spkd_ID_TIMEDATE_SET_REQUEST                      = 147;  # 0x93 - MX Speak
spkd_ID_POINT_INFO_REQUEST                        = 148;  # 0x94 - MX Speak
spkd_ID_POINT_INFO_REPLY                          = 149;  # 0x95 - MX Speak
spkd_ID_POINT_CLNT_ACKNOWLEDGE                    = 150;  # 0x96 - MX Speak
spkd_ID_REMOTE_STRING_REQUEST                     = 151;  # 0x97 - MX Speak
spkd_ID_REMOTE_STRING_REPLY                       = 152;  # 0x98 - MX Speak
spkd_ID_REMOTE_STRINGS_CHANGED                    = 153;  # 0x99
spkd_ID_EXPANDED_STRING                           = 154;  # 0x9a
spkd_ID_PANEL_INFO_TRANSFER_CONFIG                = 155;  # 0x9b
spkd_ID_POINT_MANAGER_REPLY                       = 156;  # 0x9c - used by Zetfas Bridge
spkd_ID_REPORT_REQUEST_REPLY                      = 157;  # 0x9d
spkd_ID_REPORT_REQUEST                            = 158;  # 0x9e
spkd_ID_ALOOP_INFO_REQUEST                        = 159;  # 0x9f
spkd_ID_ALOOP_INFO_REPLY                          = 160;  # 0xa0
spkd_ID_EVENT_ACTION_REGISTER_CLIENT              = 161;  # 0xa1
spkd_ID_EVENT_ACTION_DEREGISTER_CLIENT            = 162;  # 0xa2
spkd_ID_EVENT_ACTION_REGISTER_ACKNOWLEDGE         = 163;  # 0xa3
spkd_ID_EVENT_ACTION_CHANGE_CLIENT_REGISTRATION   = 164;  # 0xa4
spkd_ID_EVENT_ACTION_GROUP_DATA                   = 165;  # 0xa5
spkd_ID_EVENT_ACTION_COUNTER_REQUEST              = 166;  # 0xa6
spkd_ID_EVENT_ACTION_COUNTER_REPLY                = 167;  # 0xa7
spkd_ID_COMMS_REMOTE_NODE_STATE_CHANGE            = 168;  # 0xa8
spkd_ID_REQUEST_PRINTER_DETAILS                   = 169;  # 0xa9
spkd_ID_PRINTER_DETAILS_REQUESTED                 = 170;  # 0xaa
spkd_ID_ISOLATE_STATUS_UPDATE                     = 171;  # 0xab
spkd_ID_POINT_TEST                                = 172;  # 0xac
spkd_ID_LOOP_VERSION_INFO_REQUEST                 = 173;  # 0xad
spkd_ID_LOOP_VERSION_INFO_REPLY                   = 174;  # 0xae
spkd_ID_LOOP_POLL_INFO_REQUEST                    = 175;  # 0xaf
spkd_ID_LOOP_POLL_INFO_REPLY                      = 176;  # 0xb0
spkd_ID_RBUS_UNIT_VERSION_INFO_REQUEST            = 177;  # 0xb1
spkd_ID_RBUS_UNIT_VERSION_INFO_REPLY              = 178;  # 0xb2
spkd_ID_LOOP_SHUTDOWN_RESTART                     = 179;  # 0xb3
spkd_ID_LOOP_SHUTDOWN_RESTART_REPLY               = 180;  # 0xb4
spkd_ID_LAMP_TEST_REQUEST                         = 181;  # 0xb5
spkd_ID_RESTART_REQUEST                           = 182;  # 0xb6
spkd_ID_POINT_MANAGER_BASE                        = 183;  # 0xb7
spkd_ID_STANDARD_STATUS_REPLY                     = 184;  # 0xb8
spkd_ID_SYSTEM_STATUS_VALUES_REQUEST              = 185;  # 0xb9
spkd_ID_SYSTEM_STATUS_VALUES_REPLY                = 186;  # 0xba
spkd_ID_SYSTEM_SECTORID_FROM_ZONE_REQUEST         = 187;  # 0xbb
spkd_ID_SYSTEM_SECTORID_FROM_ZONE_REPLY           = 188;  # 0xbc
spkd_ID_FMWR_VERSION_INFO_REQUEST                 = 189;  # 0xbd
spkd_ID_FMWR_VERSION_INFO_REPLY                   = 190;  # 0xbe
spkd_ID_FAULT_INFO                                = 191;  # 0xbf
spkd_ID_BATTERY_INFO_REQUEST                      = 192;  # 0xc0
spkd_ID_BATTERY_INFO_REPLY                        = 193;  # 0xc1
spkd_ID_NAME_STRING_REQUEST                       = 194;  # 0xc2
spkd_ID_NAME_STRING_REPLY                         = 195;  # 0xc3
spkd_ID_OLD_POINT_STATE_EDGE                      = 196;  # 0xc4
spkd_ID_NEW_POINT_STATE_EDGE                      = 197;  # 0xc5
spkd_ID_POINT_STATUS_UPDATE                       = 198;  # 0xc6 - used by Zetfas Bridge
spkd_ID_POINT_CONFIGURATION_UPDATE                = 199;  # 0xc7
# These packet IDs are fixed and their values may be known
#to external developers do NOT change them.
spkd_ID_REMOTE_STATE_INFORMATION_REQUEST          = 200;  # 0xc8 - MX Speak
spkd_ID_REMOTE_STATE_INFORMATION_REPLY            = 201;  # 0xc9 - MX Speak
spkd_ID_EVENT_ACTION_ZONE_STATE_PER_ZONE_REQUEST  = 202;  # 0xca - used by Zetfas Bridge
spkd_ID_EVENT_ACTION_ZONE_STATE_PER_ZONE_REPLY    = 203;  # 0xcb - used by Zetfas Bridge
spkd_ID_CONFIGURATION                             = 204;  # 0xcc
spkd_ID_REMOTE_VERSION_INFO_REQUEST               = 205;  # 0xcd
spkd_ID_REMOTE_VERSION_INFO_REPLY                 = 206;  # 0xce
spkd_ID_EVENT_ACTION_GROUP_INFO_REQUEST           = 207;  # 0xcf
spkd_ID_EVENT_ACTION_GROUP_INFO_REPLY             = 208;  # 0xd0
spkd_ID_REMOTE_TEST_EQUIPMENT_REQUEST             = 209;  # 0xd1
spkd_ID_REMOTE_TEST_EQUIPMENT_REPLY               = 210;  # 0xd2
spkd_ID_REMOTE_TEST_EQUIPMENT_TO_PANEL_POINT_UPDATE        = 211; #   0xd3
spkd_ID_REMOTE_TEST_EQUIPMENT_TO_PANEL_POINT_UPDATE_REPLY = 212   #  0xd4
spkd_ID_POINT_MULTIPOINT_REQUEST                  = 213;  # 0xd5
spkd_ID_POINT_MULTIPOINT_REPLY                    = 214;  # 0xd6
spkd_ID_POINT_MP_ONE_SHOT_REQUEST                 = 215;  # 0xd7
spkd_ID_FIRE_RESET_SYNC_REQ_RECEIVED              = 216;  # 0xd8
spkd_ID_SPARE_ID_E                                = 217;  # 0xd9
spkd_ID_RBUS_MULTICAST                            = 218;  # 0xda
spkd_ID_PULSE_PATTERN_RESET                       = 219;  # 0xdb
spkd_ID_POINT_CONFIG_REQUEST                      = 220;  # 0xdc
spkd_ID_POINT_CONFIG_REPLY                        = 221;  # 0xdd
spkd_ID_ZONE_TEXT_UPDATE                          = 222;  # 0xde
spkd_ID_SECTOR_TEXT_UPDATE                        = 223;  # 0xdf
spkd_ID_INFO_TEXT_UPDATE                          = 224;  # 0xe0
spkd_ID_PANEL_TEXT_UPDATE                         = 225;  # 0xe1
spkd_ID_PASSWORD_TEXT_UPDATE                      = 226;  # 0xe2
spkd_ID_WRAPPED_MINERVA_PACKET                    = 227;  # 0xe3 - MX Speak
spkd_ID_COMMISSIONING_AND_SERVICE_REQUEST         = 228;  # 0xe4
spkd_ID_COMMISSIONING_AND_SERVICE_REPLY           = 229;  # 0xe5
spkd_ID_BROADCAST_LOCAL_COUNTS                    = 230;  # 0xe6, - used by Zetfas Bridge
spkd_ID_EVENT_ACTION_GROUP_DELAY                  = 231;  # 0xe7,
spkd_ID_REMOTE_MANAGER_BASE                       = 232;  # 0xe8
spkd_ID_SYSTEM_MANAGER_PACKET_BASE                = 233;  # 0xe9
spkd_ID_REMOTE_NETWORK_SYNCHRONISATION            = 234;  # 0xea
spkd_ID_DATA_TO_REMOTE_TEST_EQUIPMENT             = 235;  # 0xeb
spkd_ID_DEBUG_MANAGER_PACKET_BASE                 = 236;  # 0xec
spkd_ID_RESYNCH_REQUIRED                          = 237;  # 0xed
spkd_ID_RESYNCH_COMPLETE                          = 238;  # 0xee
spkd_ID_CONFIGURED_LOOP_DEVICE_TYPES_REQUEST      = 239;  # 0xef
spkd_ID_CONFIGURED_LOOP_DEVICE_TYPES_REPLY        = 240;  # 0xf0
spkd_ID_DEVICE_REPLACEMENT_REQUEST                = 241;  # 0xf1
spkd_ID_DEVICE_REPLACEMENT_REPLY                  = 242;  # 0xf2
spkd_ID_FORCE_PRINTER_PAUSE_UNPAUSE               = 243;  # 0xf3
# These packets is internal, not to NGUI.
spkd_ID_NGUI_FROM_DATA_SERVER_BASE                = 244;  # 0xf4
spkd_ID_NGUI_CLIENT_SERVICE_SUPPORT               = 245;  # 0xf5
spkd_ID_LOG_MANAGER_BASE                          = 246;  # 0xf6
# These packets is internal, not to NGUI.
spkd_ID_NGUI_TO_DATA_SERVER_BASE                  = 247;  # 0xf7
spkd_ID_DIGITAL_MANAGER_BASE                      = 248;  # 0xf8

#Special ID's, some used for Testing purposes...
spkd_LAST_PACKET_ID                               = 0xFFFF
