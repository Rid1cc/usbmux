# MuxConnectorAPI
## Provides methodes for usbmux
### Check out https://github.com/luk6xff/usbmux/tree/power_relays
---
#### Methodes:

``` check_mux_inf("PORT") ``` Returns device specification

``` mux_reboot("PORT") ``` Reboots device

``` switch_relay("PORT","RELAY_ID",on_off.ON/on_off.OFF) ``` Switches relay state - ON or OFF

``` get_name("PORT") ``` Returns device name

``` change_mux_name("PORT","NEW_NAME") ``` Returns device specification
