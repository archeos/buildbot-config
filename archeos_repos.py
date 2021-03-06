# These repos are checked in archeos_sources.py for modifications on ALL branches
all_branch_repos = {'archeos-manual': 'git://github.com/archeos/archeos-manual.git',
         'archeos-meta': 'git://github.com/archeos/archeos-meta.git',
         'archeos-desktop-base': 'git://github.com/archeos/archeos-desktop-base.git',
#        'test-repos': 'git://github.com/fabfurnari/test-repos.git',
         'archeos-keyring': 'git://github.com/archeos/archeos-keyring.git',
         'archeos-menu' : 'git://github.com/archeos/archeos-menu.git',
         'totalopenstation' : 'git://github.com/archeos/totalopenstation.git',
         'archeos-apt-setup': 'git@github.com:archeos/archeos-apt-setup.git'
         }

# These repos are checked in archeos_sources.py for modification only on branch master
master_repos = {'cloudcompare-archeos': 'git://github.com/archeos/cloudcompare-archeos.git',
                'micmac-archeos': 'git@github.com:archeos/micmac-archeos.git'}

# this dict must contain all repos
all_repos = dict(all_branch_repos.items() + master_repos.items())

