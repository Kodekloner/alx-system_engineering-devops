#!/usr/bin/pup
# specify a version that is compatible with Flask
package {'werkzeug':
  ensure => '2.1.1',
  provider => 'pip3',
}

# Install an especific version of flask (2.1.0)
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require => Package['werkzeug'],
}
