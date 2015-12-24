#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define	db_ver	%(rpm -q --whatprovides --qf '%%|E?{%%{E}:}|%%{V}' db-devel)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DB_File
%define		pnam	DB_File
Summary:	DB_File allows to manage a simple ASCII database
Summary(pl.UTF-8):	DB_File pozwala na korzystanie z prostej, tekstowej bazy danych
Name:		perl-DB_File
Version:	1.828
Release:	6
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/DB_File/%{pnam}-%{version}.tar.gz
# Source0-md5:	519c2056754a3b1897c6d8b3bc82d6f5
Patch0:		%{name}-rpm-automation.patch
URL:		http://search.cpan.org/dist/DB_File/
BuildRequires:	db-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	db = %{db_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DB_File is a module which allows Perl programs to make use of the
facilities provided by Berkeley DB version 1.

%description -l pl.UTF-8
DB_File jest modułem, który pozwala programom w Perlu na korzystanie
z udogodnień dostarczanych przez Berkeley DB w wersji 1.

%prep
%setup -q -n %{pnam}-%{version}
%patch0 -p1

%build
%{__perl} -pi -e "s/INSTALLDIRS => 'perl',//" Makefile.PL
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%{perl_vendorarch}/auto/DB_File/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/DB_File/DB_File.so
%{_mandir}/man3/DB_File.3pm*
