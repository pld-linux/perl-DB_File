%include	/usr/lib/rpm/macros.perl
%define		pdir	DB_File
%define		pnam	DB_File
Summary:	DB_File Perl module
Summary(cs):	Modul DB_File pro Perl
Summary(da):	Perlmodul DB_File
Summary(de):	DB_File Perl Modul
Summary(es):	Módulo de Perl DB_File
Summary(fr):	Module Perl DB_File
Summary(it):	Modulo di Perl DB_File
Summary(ja):	DB_File Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	DB_File ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul DB_File
Summary(pl):	Modu³ Perla DB_File
Summary(pt):	Módulo de Perl DB_File
Summary(pt_BR):	Módulo Perl DB_File
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl DB_File
Summary(sv):	DB_File Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl DB_File
Summary(zh_CN):	DB_File Perl Ä£¿é
Name:		perl-DB_File
Version:	1.804
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
Patch0:		%{name}-rpm-automation.patch
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DB_File allows to manage a simple ASCII database.

%description -l pl
DB_File pozwala na korzystanie z prostej, tekstowej bazy danych.

%prep
%setup -q -n %{pnam}-%{version}
%patch0 -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man3


%{__make} install DESTDIR=$RPM_BUILD_ROOT

pod2man --section 3pm DB_File.pm >$RPM_BUILD_ROOT%{_mandir}/man3/DB_File.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_archlib}/DB_File.pm
%dir %{perl_archlib}/auto/DB_File
%{perl_archlib}/auto/DB_File/DB_File.bs
%{perl_archlib}/auto/DB_File/autosplit.ix
%attr(755,root,root) %{perl_archlib}/auto/DB_File/DB_File.so
%{_mandir}/man3/*
