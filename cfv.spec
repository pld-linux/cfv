Summary:	Test and create .sfv, .csv and md5sum files
Summary(pl):	Testuje oraz tworzy pliki .sfv, .csv oraz md5sum
Name:		cfv
Version:	1.9
Release:	1
License:	GPL
Vendor:		Matt Mueller <donut@azstarnet.com>
Group:		Applications/Archiving
Source0:	http://www.azstarnet.com/~donut/programs/cfv/%{name}-%{version}.tar.gz
URL:		http://www.azstarnet.com/~donut/programs/cfv/
Requires:	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cfv is a utility to both test and create .sfv, .csv and md5sum files.
These files are commonly used to ensure the correct retrieval or
storage of data.

%description -l pl
cfv to narz�dzie do testowania i tworzenia plik�w .sfv, .csv i md5sum.
Te pliki s� cz�sto u�ywane w celu upewnienia si� o poprawnym przesyle
danych poprzez sie�.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install cfv	$RPM_BUILD_ROOT%{_bindir}
install cfv.1	$RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf Changelog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man*/*
