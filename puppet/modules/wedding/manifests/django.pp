class wedding::django {
  python::pip { 'Django':
    pkgname => 'Django',
    ensure  => '1.7.4',
    owner   => 'root',
  }
}
