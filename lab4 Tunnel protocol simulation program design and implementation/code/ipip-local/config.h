// 这里用于方便直接模拟四台主机（非真实环境下的）
#include <arpa/inet.h>
char left_net_mask[] = "255.255.255.0";
char right_net_mask[] = "255.255.255.0";
char left_net_ip[] = "172.20.10.6";
char right_net_ip[] = "172.17.37.0";

// inet_aton
