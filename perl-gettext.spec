#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-gettext
Version  : 1.07
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/P/PV/PVANDRY/gettext-1.07.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PV/PVANDRY/gettext-1.07.tar.gz
Summary  : 'Perl bindings for POSIX i18n gettext functions'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-gettext-lib = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Locale::gettext
version 1.07
This is a perl5 module quickly written to gain access to
the C library functions for internatialization. They
work just like the C versions.

%package dev
Summary: dev components for the perl-gettext package.
Group: Development
Requires: perl-gettext-lib = %{version}-%{release}
Provides: perl-gettext-devel = %{version}-%{release}

%description dev
dev components for the perl-gettext package.


%package lib
Summary: lib components for the perl-gettext package.
Group: Libraries

%description lib
lib components for the perl-gettext package.


%prep
%setup -q -n Locale-gettext-1.07

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/Locale/gettext.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Locale::gettext.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/x86_64-linux-thread-multi/auto/Locale/gettext/gettext.so
