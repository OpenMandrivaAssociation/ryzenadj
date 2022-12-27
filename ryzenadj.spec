Name:		ryzenadj
Version:	0.12.0
Release:	1
License:	GPLv3
Summary:	Adjust power management settings for Ryzen Mobile Processors
Group:		System/Configuration/Hardware
Url:		https://github.com/FlyGoat/RyzenAdj
Source0:	https://github.com/FlyGoat/RyzenAdj/archive/v%{version}/RyzenAdj-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig(libpci)
Provides:	RyzenAdj = %{EVRD}

%description
Adjust power management settings for Ryzen Mobile Processors.

#------------------------------------------------------------------

%prep
%autosetup -p1 -n RyzenAdj-%{version}

%build
%cmake \
	-DBUILD_SHARED_LIBS=OFF
%make_build

# There is no instal target. Let's install files manually.
#install
#make_install -C build

%install
mkdir -p %{buildroot}%{_bindir}
install -D -m0755 build/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/ryzenadj
