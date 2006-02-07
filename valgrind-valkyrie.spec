Summary:	Valkyrie GUI and XML merging tool for Memcheck outputs
Name:		valgrind-valkyrie
Version:	1.1.0
Release:	0.1
License:	GPL v2, GFDL (docs)
Group:		Development/Tools
Source0:	http://valgrind.org/downloads/valkyrie-%{version}.tar.bz2
# Source0-md5:	b49d73801b49521af1c05c3f4ae2712f
Patch0:		%{name}-sh.patch
URL:		http://valgrind.org/
BuildRequires:	qt-devel
Requires:	valgrind >= 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Valkyrie is a GPL'd graphical front-end to the Valgrind suite of tools
for debugging and profiling x86-Linux programs.

Valkyrie includes an auxiliary tool which can read XML output from
multiple valgrind (memcheck) runs, merge them together into a single
XML file, and optionally display the merged result in the GUI.

%prep
%setup -q -n valkyrie-%{version}
%patch0 -p1

%build
# not automake generated configure
./configure \
	--prefix=%{_prefix} \
	--bindir=%{_bindir} \
	--docdir=%{_docdir}/%{name}-%{version} \
	--vg-dir=%{_prefix} \
	--qt-dir=%{_prefix} \
	--qt-lib=%{_libdir} \
	--shared

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
