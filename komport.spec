Summary:	Serial port communications and vt102 terminal emulator for KDE
Summary(pl.UTF-8):	Program do komunikacji przez port szeregowy i emulator terminala vt102 dla KDE
Name:		komport
Version:	0.5.9
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/komport/%{name}-%{version}.tar.gz
# Source0-md5:	215bab736190d6150988bc39929a846d
Source1:	%{name}.desktop
URL:		http://komport.sourceforge.net/
BuildRequires:	kdelibs-devel
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Serial port communications and vt102 terminal emulator for KDE. Aim of
the project is to provide an alternative to minicom, and with a KDE
style user interface.

komport is a minicom-like serial terminal emulator with scripting
support. The requirement for this program was to be small enough to
fit on a floppy-based Linux distribution - such as the one from Linux
Router Project.

%description -l pl.UTF-8
Program do komunikacji przez port szeregowy i emulator terminala vt102
dla KDE. Celem projektu jest dostarczenie alternatywy dla minicoma z
interfejsem użytkownika w stylu KDE.

komport to emulator terminala szeregowego podobny do minicoma z
obsługą skryptów. Wymagania tego programu miały być tak małe, by
mieścił się na dyskietkowych dystrybucjach Linuksa - takich jak ta z
projektu Linux Router Project.

%prep
%setup -q

%build
rm -f komport/settingsdialog.[ch]
%configure2_13 \
	--enable-final \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}/kde

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/kde

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/komport
%{_iconsdir}/*/*/*/*.png
%{_desktopdir}/kde/*.desktop
