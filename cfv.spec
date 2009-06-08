Summary:	Test and create .sfv, .csv and md5sum files
Summary(pl.UTF-8):	Testuje oraz tworzy pliki .sfv, .csv oraz md5sum
Name:		cfv
Version:	1.18.3
Release:	1
License:	GPL v2+
Vendor:		Matt Mueller <donut@azstarnet.com>
Group:		Applications/Archiving
Source0:	http://dl.sourceforge.net/cfv/%{name}-%{version}.tar.gz
# Source0-md5:	1be9039c2ab859103d70b6c4f4e5edf5
URL:		http://cfv.sourceforge.net/
Requires:	python
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cfv is a utility to both test and create .sfv, .csv and md5sum files.
These files are commonly used to ensure the correct retrieval or
storage of data.

%description -l pl.UTF-8
cfv to narzędzie do testowania i tworzenia plików .sfv, .csv i md5sum.
Te pliki są często używane w celu upewnienia się o poprawnym przesyle
danych poprzez sieć.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install cfv	$RPM_BUILD_ROOT%{_bindir}
install cfv.1	$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
