%include	/usr/lib/rpm/macros.perl
Summary:	DB_File perl module
Summary(pl):	Modu³ perla DB_File
Name:		perl-DB_File
Version:	1.79
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/DB_File/DB_File-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DB_File allows to manage a simple ASCII database.

%description -l pl
DB_File pozwala na korzystanie z prostej, tekstowej bazy danych.

%prep
%setup -q -n DB_File-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_archlib}/DB_File.pm
%dir %{perl_archlib}/auto/DB_File
%{perl_archlib}/auto/DB_File/autosplit.ix
%{perl_archlib}/auto/DB_File/DB_File.bs
%attr(755,root,root) %{perl_archlib}/auto/DB_File/DB_File.so
