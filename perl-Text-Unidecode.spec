%{?scl:%scl_package perl-Text-Unidecode}
%{!?scl:%global pkg_name %{name}}

Name:           %{?scl_prefix}perl-Text-Unidecode
Version:        0.04
Release:        2.sc1%{?dist}
Summary:        US-ASCII transliterations of Unicode text

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Text-Unidecode/
Source0:        http://www.cpan.org/modules/by-module/Text/Text-Unidecode-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(integer)
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(Test)
BuildRequires:  %{?scl_prefix}perl(utf8)
BuildRequires:  %{?scl_prefix}perl(vars)
%{?scl:%global perl_version %(scl enable %{scl} 'eval "`perl -V:version`"; echo $version')}
%{!?scl:%global perl_version %(eval "`perl -V:version`"; echo $version)}
Requires:  %{?scl_prefix}perl(:MODULE_COMPAT_%{perl_version})

%description

Text::Unidecode provides a function, `unidecode(...)' that
takes Unicode data and tries to represent it in US-ASCII
characters (i.e., the universally displayable characters between
0x00 and 0x7F). The representation is almost always an attempt at
*transliteration* -- i.e., conveying, in Roman letters, the
pronunciation expressed by the text in some other writing
system. 

%prep
%setup -q -n Text-Unidecode-%{version}

%build
%{?scl:scl enable %{scl} "}
perl Makefile.PL INSTALLDIRS=vendor
%{?scl:"}
%{?scl:scl enable %{scl} "}
make %{?_smp_mflags}
%{?scl:"}

%install
rm -rf $RPM_BUILD_ROOT
%{?scl:scl enable %{scl} "}
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{?scl:"}
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} "}
make test
%{?scl:"}

%files
%doc README TODO.txt ChangeLog
%{perl_vendorlib}/Text/
%{_mandir}/man3/*.3*


%changelog
* Wed Nov 13 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-2
- Update dependencies

* Tue Apr 02 2013 Jitka Plesnikova <jplesnik@redhat.com> - 0.04-1
- SCL package - initial import
