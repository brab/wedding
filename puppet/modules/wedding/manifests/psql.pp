class wedding::psql {
  class { 'postgresql::server': }
  class { 'postgresql::lib::devel': }

  postgresql::server::role { 'wedding_user':
    password_hash => postgresql_password('wedding_user', 'iecoojaB7chu7eig_u8queifohbi'),
  }

  postgresql::server::db { 'wedding':
    user     => 'wedding_user',
    password => postgresql_password('wedding_user', 'iecoojaB7chu7eig_u8queifohbi'),
  }

  postgresql::server::database_grant { 'wedding':
    privilege => 'ALL',
    db        => 'wedding',
    role      => 'wedding_user',
  }
}
