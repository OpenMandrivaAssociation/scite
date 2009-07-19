%define name 	scite
%define version 1.79
%define release %mkrel 2
%define libname %mklibname scintilla 1
%define develname %mklibname -d scintilla

%define scitever %(echo %{version} | sed -e 's/\\.//')

Summary: 	GTK text editor based on scintilla
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Editors
Url: 		http://www.scintilla.org/SciTE.html
Source: 	http://prdownloads.sourceforge.net/scintilla/scite%scitever.tgz
Source1:	scintilla.cmake
Source2:	scite.cmake
Source3:	scintilla.pc.cmake
Requires:	%{libname} = %version-%release
BuildRoot: 	%{_tmppath}/%{name}-root
BuildRequires: 	gtk+2-devel pkgconfig
BuildRequires:	desktop-file-utils

%description
SciTE is a GTK based single-document editor.  While its features are
limited, its main purpose is to show off scintilla, an extensible
text highlighting and formatting engine.

%package -n %{libname}
Summary:	Shared libraries required to run SciTE
Group:		System/Servers

%description -n %{libname}
This package contains shared libraries used by SciTE.

%package -n	%{develname}
Group:		Development/C
Summary:	Headers and static lib for scintilla development
Requires:	%{libname} = %{version}-%{release}
Provides:	scintilla-devel = %{version}-%{release}

%description -n	%{develname}
Install this package if you want do compile applications using the
scintilla library.

%prep
rm -fr $RPM_BUILD_DIR/scintilla
%setup -q -n scite
cp %SOURCE1 $RPM_BUILD_DIR/scintilla/CMakeLists.txt
cp %SOURCE3 $RPM_BUILD_DIR/scintilla/scintilla.pc.cmake
cp %SOURCE2 $RPM_BUILD_DIR/scite/CMakeLists.txt

%build
cd $RPM_BUILD_DIR/scintilla
%{cmake}
%make

cd $RPM_BUILD_DIR/scite
perl -p -i -e 's/netscape/www-browser/g' ../src/Embedded.properties
perl -p -i -e 's/netscape/www-browser/g' ../src/html.properties
perl -p -i -e 's/netscape/www-browser/g' ../src/SciTEGlobal.properties
%{cmake}
%make

%install
cd $RPM_BUILD_DIR/scintilla/build
%{makeinstall_std}

cd $RPM_BUILD_DIR/scite/build
%{makeinstall_std}

desktop-file-install --vendor='' \
	--dir=%buildroot%_datadir/applications \
	--remove-category='Application' \
	%buildroot%_datadir/applications/*.desktop

%clean
rm -fr $RPM_BUILD_ROOT $RPM_BUILD_DIR/scintilla

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-,root,root)
%doc doc/*
%_bindir/SciTE
%_datadir/%name
%_datadir/pixmaps/*
%_datadir/applications/*
%_mandir/man1/*

%files -n %{libname}
%defattr(644, root, root)
%{_libdir}/libscintilla.so
%{_libdir}/libscintilla.so.1.79

%files -n %{develname}
%defattr(644, root, root)
%dir %{_includedir}/scintilla
%{_libdir}/pkgconfig/scintilla.pc
%{_includedir}/scintilla/*.h
