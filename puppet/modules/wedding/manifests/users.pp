class wedding::users {
  user { 'brab':
    ensure => present,
    shell  => '/bin/bash',
  } ->
  file { 'home brab':
    path   => '/home/brab',
    ensure => directory,
    owner  => 'brab',
    group  => 'brab',
    mode   => 700,
  }
  file { 'sudoers brab':
    path   => '/etc/sudoers.d/brab',
    source => 'puppet:///modules/wedding/sudoers/brab',
    ensure => present,
    owner  => 'root',
    group  => 'root',
    mode   => 440,
  }
}
