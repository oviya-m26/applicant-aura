import Logo from "../assets/india_flag.svg"
const ApplicantAuraLogo = ({ className }) => {
  return (
    <>
      <img
        src={Logo}
        alt="ApplicantAura, Job tracking web app"
        className={` ${className} object-cover mix-blend-multiply  `}
      />
    </>
  )
}

export default ApplicantAuraLogo
