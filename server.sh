su
apt install mariadb-client mariadb-server -y
apt install apache2 libapache2-mod-php7.0 -y
apt install php7.0 php7.0-mysql libapache2-mod-php7.0 -y
apt install php7.0-xml php7.0-zip php7.0-xmlrpc -y
apt install php7.0-readline php7.0-snmp php7.0-soap -y
apt install php7.0-odbc php7.0-opcache php7.0-mbstring -y
apt install php7.0-mcrypt php7.0-ldap php7.0-json php7.0-intl -y
apt install php7.0-imap php7.0-interbase php-all-dev php7.0 -y
apt install php7.0-curl php7.0-common php7.0-cli php7.0-cgi php7.0-bz2 -y
/etc/init.d/apache2 restart
mysql -u root -p
#MariaDB [(none)]> CREATE USER 'wpuser'@'localhost' IDENTIFIED BY 'wppass';
#MariaDB [(none)]> CREATE DATABASE wp_database;
#MariaDB [(none)]> GRANT ALL ON `wp_database`.* TO `wpuser`@`localhost`;
#MariaDB [(none)]> FLUSH PRIVILEGES;
#MariaDB [(none)]> exit;
cd /var/www/html/
wget https://wordpress.org/latest.tar.gz
tar xpf latest.tar.gz
chown -R www-data:www-data /var/www/html
find /var/www/html/wordpress/ -type d -exec chmod 755 {} \;
find /var/www/html/wordpress/ -type f -exec chmod 644 {} \;
a2enmod rewrite
/etc/init.d/apache2 restart
nano /etc/apache2/sites-available/000-default.conf
/etc/init.d/apache2 restart

#<Directory /var/www/html>
#        Options Indexes FollowSymLinks
#        AllowOverride All
#        Require all granted
#</Directory>
