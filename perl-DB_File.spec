%include	/usr/lib/rpm/macros.perl
Summary:	DB_File perl module
Summary(pl):	Modu³ perla DB_File
Name:		perl-DB_File
Version:	1.804
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/DB_File/DB_File-%{version}.tar.gz
Patch0:		%{name}-rpm-automation.patch
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DB_File allows to manage a simple ASCII database.

%description -l pl
DB_File pozwala na korzystanie z prostej, tekstowej bazy danych.

%prep
%setup -q -n DB_File-%{version}
%patch0 -p1

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_archlib}/DB_File.pm
%dir %{perl_archlib}/auto/DB_File
%{perl_archlib}/auto/DB_File/autosplit.ix
%{perl_archlib}/auto/DB_File/DB_File.bs
%attr(755,root,root) %{perl_archlib}/auto/DB_File/DB_File.so
