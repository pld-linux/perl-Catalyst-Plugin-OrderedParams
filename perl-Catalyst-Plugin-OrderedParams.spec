#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Plugin-OrderedParams
Summary:	Catalyst::Plugin::OrderedParams - Maintain order of submitted form parameters
Summary(pl):	Catalyst::Plugin::OrderedParams - zarz±dzenie kolejno¶ci± parametrów formularzy
Name:		perl-Catalyst-Plugin-OrderedParams
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	362c08e2434656044e64d3d66ae025f9
URL:		http://search.cpan.org/dist/Catalyst-Plugin-OrderedParams/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst >= 5.30
BuildRequires:	perl-Tie-Hash-Indexed
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin enables handling of GET and POST parameters in an ordered
fashion. By default in Catalyst, form parameters are stored in a
simple hash, which loses the original order in which the parameters
were submitted. This plugin stores parameters in a Tie::IxHash which
will retain the original submitted order.

%description -l pl
Ta wtyczka pozwala obs³ugiwaæ parametry GET i POST w sposób
uporz±dkowany. Domy¶lnie w Cataly¶cie parametry formularzy s±
przechowywane w prostym haszu, który traci oryginaln± kolejno¶æ, w
jakiej parametry zosta³y przekazane. Ta wtyczka przechowuje parametry
w strukturze Tie::IxHash, która zachowuje oryginaln± kolejno¶æ
przekazanych parametrów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Catalyst/Plugin/*.pm
%{_mandir}/man3/*
