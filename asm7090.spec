Name:           asm7090
Version:        2.3.2
Release:        1%{?dist}
Summary:        IBM 7090 cross-assembler
License:        MIT
URL:            https://www.cozx.com/dpitts/ibm7090.html
Source0:        https://www.cozx.com/dpitts/tarballs/ibm709x/%{name}-%{version}.tar.gz
Patch0:         asm7090-2.3.2-gcc15.patch
Patch1:         asm7090-2.3.2-make.patch

BuildRequires:  gcc
BuildRequires:  make


%description
asm7090 is a cross assembler for the IBM 7090 and 7094 computer. It is MAP and
FAP compatible and supports absolute and relocatable assembly. Macros and
conditional assembly are supported. The floating and binary point conversion
for the DEC pseudo op was corrected and supports double precision.  Also,
supported is the FAP mode of assembly and supports multiple assemblies in a
single files as FAP does.  Supports the 7090 macros for 7094 instructions and
CPU model checks.

If IBSYS control cards are at the beginning of assembly source the TITLE and
IBMAP fields are parsed and used to set the appropriate options in the assembly
of the module. The EXECUTE IBSFAP control card is parsed to allow support of
FAP assemblies. The control cards are listed in the listing on a seperate page.

Also supported are the CTSS instructions and pseudo operation codes.


%prep
%autosetup -n %{name}


%build
# parallel make doesn't work
make DEBUG="%{build_cflags}" LDFLAGS="%{build_ldflags}"


%install
mkdir -p %{buildroot}%{_bindir}
make install INSTDIR=%{buildroot}%{_bindir}


%files
%license LICENSE.txt
%doc README.txt
%{_bindir}/%{name}


%changelog
* Sun Oct 19 2025 Dan Horák <dan[at]danny.cz> - 2.3.2-1
- initial Fedora version
