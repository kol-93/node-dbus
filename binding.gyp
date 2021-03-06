{
  'targets': [
    {
      'target_name': 'dbus',
      'sources': [
        'src/dbus.cc',
        'src/connection.cc',
        'src/signal.cc',
        'src/encoder.cc',
        'src/decoder.cc',
        'src/introspect.cc',
        'src/object_handler.cc'
      ],
      'include_dirs': [
        "<!(node -e \"require('nan')\")"
      ],
      'dependencies': [
        'deps/libexpat/libexpat.gyp:expat'
      ],
      'conditions': [
        ['OS=="linux"', {
          'defines': [
            'LIB_EXPAT=expat'
          ],
          'cflags': [
            '-std=gnu++0x',
            '<!@(pkg-config --cflags dbus-1)'
          ],
          'ldflags': [
            '<!@(pkg-config  --libs-only-L --libs-only-other dbus-1)'
          ],
          'libraries': [
            '<!@(pkg-config  --libs-only-l --libs-only-other dbus-1)'
          ]
        }],
        ['OS=="mac"', {
          'include_dirs': [
            '<!@(pkg-config --cflags-only-I dbus-1 | sed s/-I//g)'
          ],
          'ldflags': [
            '<!@(pkg-config  --libs-only-L --libs-only-other dbus-1)'
          ],
          'libraries': [
            '<!@(pkg-config  --libs-only-l --libs-only-other dbus-1)'
          ]
        }],
        ['OS=="win"', {
        	'cflags': [
        		'-std=c++11'
        	],
        	'libraries': [
        		'-ldbus-1.lib'
        	]
        }]
      ]
    }
  ]
}
