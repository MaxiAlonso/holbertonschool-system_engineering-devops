# Task 0


exec {'change open files limit':
  command => 'sed -i "s/15/2000/" /etc/default/nginx; service nginx restart',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  }
