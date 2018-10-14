# weechat
sudo sh -c 'echo "deb https://weechat.org/ubuntu $(lsb_release -cs) main" >> /etc/apt/sources.list.d/weechat.list'
sudo apt-key adv --keyserver keys.gnupg.net --recv-keys 11E9DE8848F2B65222AA75B8D1820DB22A11534E
sudo apt-get upgrade
sudo apt-get install weechat
mkdir .weechat
openssl ecparam -genkey -name prime256v1 -out ~/.weechat/ecdsa.pem
openssl ec -noout -text -conv_form compressed -in ~/.weechat/ecdsa.pem | grep '^pub:' -A 3 | tail -n 3 | tr -d ' \n:' | xxd -r -p | base64
# start client
weechat
# configure server
/unset irc.server.freenode.sasl_mechanism
/set irc.server.freenode.sasl_username REGISTERED_NICKNAME (e.g. dsikar)
/set irc.server.freenode.sasl_password PASSWORD (e.g. bananasRus)
/save
/connect
/disconnect
/quit

# irssi
sudo apt-get install irssi irssi-scripts screen openssh-server
# start client
irssi

/network add -sasl_username <login> -sasl_password <password> -sasl_mechanism PLAIN freenode 
/server add -auto -net freenode -ssl -ssl_verify chat.freenode.net 6697 
/save
/connect
/disconnect
/quit

# NB file ~/.irssi/config may need editing, changing freenode port to 6697 e.g.
#    address = "chat.freenode.net";
#    chatnet = "Freenode";
#    port = "6697";

