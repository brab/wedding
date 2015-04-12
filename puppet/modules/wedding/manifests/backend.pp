class wedding::backend {
  python::requirements { '/home/vagrant/wedding/requirements.txt':
    owner => 'root',
  }

  python::pip { 'ipython':
    pkgname => 'ipython',
    ensure  => 'latest',
    owner   => 'root'
  }

  python::pip { 'pyinotify':
    pkgname => 'pyinotify',
    ensure  => 'latest',
    owner   => 'root'
  }

  python::pip { 'django-debug-toolbar':
    pkgname => 'django-debug-toolbar',
    ensure  => 'latest',
    owner   => 'root'
  }
}
