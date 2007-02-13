#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DB_File
%define		pnam	DB_File
Summary:	DB_File allows to manage a simple ASCII database
Summary(pl.UTF-8):	DB_File pozwala na korzystanie z prostej, tekstowej bazy danych
Name:		perl-DB_File
Version:	1.814
Release:	2
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}-%{version}.tar.gz
# Source0-md5:	5ae102fe172f2aaf771a8d9cae23ca3a
Patch0:		%{name}-rpm-automation.patch
BuildRequires:	db-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DB_File is a module which allows Perl programs to make use of the
facilities provided by Berkeley DB version 1.

%description -l pl.UTF-8
DB_File jest modułem, który pozwala programom w Perlu na korzystanie
z udogodnień, dostarczanych przez Berkeley DB w wersji 1.

%prep
%setup -q -n %{pnam}-%{version}
%patch0 -p1

%build
%{__perl} -pi -e "s/INSTALLDIRS => 'perl',//" Makefile.PL
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

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
