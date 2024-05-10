%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6ThreadWeaver
%define devname %mklibname KF6ThreadWeaver -d
#define git 20240217

Name: kf6-threadweaver
Version: 6.2.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/threadweaver/-/archive/master/threadweaver-master.tar.bz2#/threadweaver-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/frameworks/%{major}/threadweaver-%{version}.tar.xz
%endif
Summary: Helper for multithreaded programming
URL: https://invent.kde.org/frameworks/threadweaver
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6Xml)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
Requires: %{libname} = %{EVRD}

%description
Helper for multithreaded programming

%package -n %{libname}
Summary: Helper for multithreaded programming
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Helper for multithreaded programming

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Helper for multithreaded programming

%prep
%autosetup -p1 -n threadweaver-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files

%files -n %{devname}
%{_includedir}/KF6/ThreadWeaver
%{_libdir}/cmake/KF6ThreadWeaver
%{_qtdir}/doc/KF6ThreadWeaver.*

%files -n %{libname}
%{_libdir}/libKF6ThreadWeaver.so*
