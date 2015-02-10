class wedding {
  class { 'stdlib': }

  class { 'apt': }
  class { 'apt::unattended_upgrades':
    update    => '1',
    upgrade   => '1',
    autoclean => '7',
  }

  class { 'python':
    version => 'system',
    pip     => true,
  }

  class { 'wedding::users': }
  class { 'wedding::psql': }
}
