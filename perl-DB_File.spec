%include	/usr/lib/rpm/macros.perl
%define	pdir	DB_File
%define	pnam	DB_File
Summary:	DB_File allows to manage a simple ASCII database
Summary(pl):	DB_File pozwala na korzystanie z prostej, tekstowej bazy danych
Name:		perl-DB_File
Version:	1.806
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
Patch0:		%{name}-rpm-automation.patch
BuildRequires:	db-devel
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DB_File is a module which allows Perl programs to make use of the
facilities provided by Berkeley DB version 1.

%description -l pl
DB_File jest modu�em, kt�ry pozwala programom w Perlu na korzystanie
z udogodnie�, dostarczanych przez Berkeley DB w wersji 1.

%prep
%setup -q -n %{pnam}-%{version}
%patch0 -p1

%build
%{__perl} -pi -e "s/INSTALLDIRS => 'perl',//" Makefile.PL
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/DB_File.pm
%dir %{perl_vendorarch}/auto/DB_File
%{perl_vendorarch}/auto/DB_File/DB_File.bs
%{perl_vendorarch}/auto/DB_File/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/DB_File/DB_File.so
%{_mandir}/man3/*
