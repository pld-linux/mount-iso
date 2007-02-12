Summary:	Mount ISO image
Summary(pl.UTF-8):   Program do montowania obrazów płyt
Name:		mount-iso
Version:	0.9.1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.kde-apps.org/content/files/11577-%{name}-%{version}.tar.bz2
# Source0-md5:	b8ef4831b525d575c6317b5df9eb777b
URL:		http://www.kde-apps.org/content/show.php?content=11577
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mount ISO Image is an advanced script which allows to perform multiple
operations with ISO, NRG (Nero Burning ROM), UDF (DVD), CUE/BIN,
CCD/IMG/SUB (CloneCD), XDVDFS (XBOX) images.

%description -l pl.UTF-8
Mount ISO Image jest zaawansowanym skryptem, który pozwala na
wykonywanie wielu operacji na plikach ISO, NRG (Nero Burning ROM), UDF
(DVD), CUE/BIN, CCD/IMG/SUB (CloneCD), XDVDFS (XBOX) będącymi
obrazami płyt.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install install.sh	$RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/install.sh
