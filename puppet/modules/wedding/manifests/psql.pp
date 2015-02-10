class wedding::psql {
  class { 'postgresql::server': }

  postgresql::server::db { 'wedding':
    user     => 'wedding_user',
    password => postgresql_password('wedding_user', 'iecoojaB7chu7eig_u8queifohbi'),
  }
}
