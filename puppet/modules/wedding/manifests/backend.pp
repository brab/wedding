class wedding::backend {
  python::requirements { '/home/vagrant/wedding/requirements.txt':
    owner => 'root',
  }

  python::pip { 'gunicorn':
    pkgname => 'gunicorn',
    ensure  => 'latest',
    owner   => 'root'
  }

  python::pip { 'ipython':
    pkgname => 'ipython',
    ensure  => 'latest',
    owner   => 'root'
  }
}
