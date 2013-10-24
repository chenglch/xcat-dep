#
# spec file for package perl-Crypt-Blowfish
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%bcond_with opt

Name:           perl-Crypt-Blowfish
Version:        2.14
Release:        5.1
%define cpan_name Crypt-Blowfish
Summary:        Perl Blowfish encryption module
License:        BSD-3-Clause
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Crypt-Blowfish/
Source:         http://www.cpan.org/authors/id/D/DP/DPARIS/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%if %{with opt}
BuildRequires:  perl(Crypt::CBC)
%endif
%if 0%{?suse_version} > 1010
Recommends:     perl(Crypt::CBC)
%endif
%{perl_requires}

%description
Blowfish is capable of strong encryption and can use key sizes up to 56
bytes (a 448 bit key). You're encouraged to take advantage of the full key
size to ensure the strongest encryption possible from this module.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes COPYRIGHT README

%changelog
* Sat Jul 27 2013 coolo@suse.com
- updated to 2.14
  - quick mod to keep META.yml current
  - updated SvUPGRADE to a statement
  - patched for WIN64
- obsoletes svupgrade.patch
* Fri Jun 21 2013 coolo@suse.com
- use source url
- add svupgrade.patch from RT#83924
* Fri Nov 18 2011 coolo@suse.com
- use original .tar.gz
* Fri Aug 26 2011 chris@computersalat.de
- cpanspec
- added bcond_with opt
  o test optional pkgs via local build (osc build --with opt)
* Sun Dec  5 2010 coolo@novell.com
- avoid build cycle
* Wed Dec  1 2010 coolo@novell.com
- switch to perl_requires macro
* Wed Nov 24 2010 chris@computersalat.de
- recreated by cpanspec 1.78
  o fix deps
- removed old Obsoletes/Provides perl_bf
- removed old Conflicts perl_cpx perl-Cryptix
* Tue Oct 19 2010 coolo@novell.com
- add perl as explicit buildrequire
* Fri Mar 26 2010 anicka@suse.cz
- update to 2.12
  * updated Changes to mesh with revision.
  * patched _blowfish.c to stop spurious warnings.
  * updated POD
- remove the patch (fixed in upstream)
* Sun Jan 10 2010 jengelh@medozas.de
- enable parallel build
* Fri Feb 10 2006 anicka@suse.cz
- remove perl-Crypt-CBC from BuildRequires
  (break the dependency cycle, CBC test will not run any more)
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Wed Jan  4 2006 anicka@suse.cz
- update to 2.10
* Sat Jan 10 2004 adrian@suse.de
- build as user
* Fri Aug 22 2003 mjancar@suse.cz
- require the perl version we build with
* Tue Jul 15 2003 mjancar@suse.cz
- adapt to perl-5.8.1
- use %%perl_process_packlist
* Wed Jun 18 2003 mjancar@suse.cz
- fix filelist
* Tue May 20 2003 mjancar@suse.cz
- remove unpackaged files
* Tue Jul  2 2002 mls@suse.de
- remove race in .packlist generation
* Tue Jan 22 2002 rvasice@suse.cz
- spec file cleanup - use predefined macros
* Thu Jan  3 2002 cihlar@suse.cz
- update to version 2.09
* Tue Mar 13 2001 cihlar@suse.cz
- reanmed perl_bf -> perl-Crypt-Blowfish
- added BuildRoot
- fixed file list
- update to version 2.06
* Thu Sep 21 2000 ro@suse.de
- fixed for perl 5.6
- bzipped source
* Tue May 23 2000 ug@suse.de
- Conflicts with perl_cpx added to spec-file
* Tue May 23 2000 ug@suse.de
- added for US distribution
