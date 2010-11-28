# NB! building this spec (currently) as root will nuke your /usr/bin directory ;)
Summary:	Valkyrie GUI and XML merging tool for Memcheck outputs
Summary(pl.UTF-8):	Vaklyrie - graficzny interfejs i narzędzie do łączenia XML dla wyjścia z Memchecka
Name:		valgrind-valkyrie
Version:	2.0.0
Release:	0.1
License:	GPL v2, GFDL (docs)
Group:		Development/Tools
Source0:	http://valgrind.org/downloads/valkyrie-%{version}.tar.bz2
# Source0-md5:	a411dfb803f548dae5f988de0160aeb5
URL:		http://valgrind.org/
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtXml-devel
Requires:	valgrind >= 3.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Valkyrie is a GPL'd graphical front-end to the Valgrind suite of tools
for debugging and profiling x86-Linux programs.

Valkyrie includes an auxiliary tool which can read XML output from
multiple valgrind (memcheck) runs, merge them together into a single
XML file, and optionally display the merged result in the GUI.

%description -l pl.UTF-8
Valkyrie to dostępny na licencji GPL graficzny interfejs do Valgrinda
- zestawu narzędzi do diagnostyki i profilowania programów linuksowych
na architekturze x86.

Valkyrie zawiera pomocnicze narzędzie, które odczytuje wyjście w XML-u
z wielu uruchomień valgrinda (memchecka), łączy je w pojedynczy plik
XML i opcjonalnie wyświetla wynik łączenia w graficznym interfejsie.

%prep
%setup -q -n valkyrie-%{version}

%build
qmake-qt4 \
	PREFIX=%{_prefix} \
	BINDIR=%{_bindir} \
	DATADIR=%{_datadir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/valkyrie-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README doc/*.html doc/images
%attr(755,root,root) %{_bindir}/valkyrie
