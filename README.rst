Clipbucket - Video sharing
==========================

`ClipBucket`_ is an OpenSource Multimedia Management application
that comes with all the bells & whistles required to start your own
Video Sharing website like Youtube or Metacafe. ClipBucket is a
versatile, scalable media distribution platform with latest social
networking features.

This appliance includes all the standard features in
`TurnKey Core`_, and on top of that:

- ClipBucket configurations:
   
   - Installed from upstream source code to /var/www/clipbucket
   - Tweaked configuration for quick and server friendly conversion,
     as well as enabled Crons and ffmpeg VF for convenience.
   - Media packages installed from deb-multimedia, and added to APT.

- SSL support out of the box.
- `PHPMyAdmin`_ administration frontend for MySQL (listening on
  port 12322 - uses SSL).
- Postfix MTA (bound to localhost) to allow sending of email
  (e.g., password recovery).
- Webmin modules for configuring Apache2, PHP, MySQL and Postfix.


Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, MySQL, phpMyAdmin: username **root**
-  ClipBucket: username **admin**

.. _ClipBucket: http://clip-bucket.com/
.. _TurnKey Core: http://www.turnkeylinux.org/core
.. _PHPMyAdmin: http://www.phpmyadmin.net
